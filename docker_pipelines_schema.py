PARENT_JOB_TEMPLATE = """
image: docker:20.10.24
services:
  - docker:20.10.24-dind
stages:
  - build
  - deploy
before_script:
  - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
"""

BUILD_JOB_TEMPLATE = """
build_{image}:
  stage: build
  variables:
    IMAGE_NAME: {image}
    GIT_SUBMODULE_STRATEGY: recursive
  script:
    - docker pull $CI_REGISTRY_IMAGE/$IMAGE_NAME:latest || true
    - >
      docker build
      --pull
      --cache-from $CI_REGISTRY_IMAGE/$IMAGE_NAME:latest
      --tag $CI_REGISTRY_IMAGE/$IMAGE_NAME:$CI_COMMIT_SHA
      images/$IMAGE_NAME/
    - docker push $CI_REGISTRY_IMAGE/$IMAGE_NAME:$CI_COMMIT_SHA
"""

DEPLOY_JOB_TEMPLATE = """
deploy_{image}:
  stage: deploy
  needs: ["build_{image}"]
  rules:
    - if: $CI_COMMIT_BRANCH == $CI_DEFAULT_BRANCH
  variables:
    IMAGE_NAME: {image}
    GIT_STRATEGY: none
  script:
    - docker pull $CI_REGISTRY_IMAGE/$IMAGE_NAME:$CI_COMMIT_SHA
    - docker tag $CI_REGISTRY_IMAGE/$IMAGE_NAME:$CI_COMMIT_SHA $CI_REGISTRY_IMAGE/$IMAGE_NAME:latest
    - docker push $CI_REGISTRY_IMAGE/$IMAGE_NAME:latest
"""
