"""This smal utility will generate 1 build job for each folder in this repository: If the target
branch is the master/main branch, then it will generate a deploy job as well."""
import argparse
import os

import gitlab

from docker_pipelines_schema import *


class PipelineWriter:
    @staticmethod
    def parent_job_template():
        return PARENT_JOB_TEMPLATE

    @staticmethod
    def build_job_template(image):
        return BUILD_JOB_TEMPLATE.format(image=image)

    @staticmethod
    def deploy_job_template(image):
        return DEPLOY_JOB_TEMPLATE.format(image=image)


def generate_ci_config() -> str:
    payload = ""
    payload += PipelineWriter.parent_job_template()
    for image in os.listdir("images"):
        if image == "pi_ros":
            print("[WARNING] This is still work in progreso, skip pi_ros for now")
            continue
        payload += PipelineWriter.build_job_template(image)
        payload += PipelineWriter.deploy_job_template(image)
    return payload


def get_pipelines_filename() -> str:
    """Get filename from the exterior world."""
    parser = argparse.ArgumentParser()
    parser.add_argument("docker_pipelines_yaml")
    args = parser.parse_args()
    return args.docker_pipelines_yaml


def run_ci_linter(content: str):
    # To test locally uncomment this line, and create your own ~/.python-gitlab.cfg
    #  gl = gitlab.Gitlab.from_config("ipb_gitlab")
    gl = gitlab.Gitlab(
        url="https://gitlab.ipb.uni-bonn.de",
        private_token=os.environ["DOCKER_BOT_PRIVATE_TOKEN"],
    )
    gl.auth()
    result = gl.http_post("/projects/1437/ci/lint", post_data={"content": content})
    # Inmediatly fail if config file is wrong
    if not result["valid"]:
        print(ci_config)
        raise Exception("Invalid CI/CD configuration file", result["errors"])


if __name__ == "__main__":
    # First thing is to generate the CI/CD config string
    ci_config = generate_ci_config()

    # Then we check everything is alright
    run_ci_linter(content=ci_config)
    # Once everything is set, we dump to disk
    with open(get_pipelines_filename(), "w+") as f:
        f.write(ci_config)
