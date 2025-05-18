import os
import subprocess

def list_local_repos(base_path="./repos"):
    repos = []
    for entry in os.listdir(base_path):
        full_path = os.path.join(base_path, entry)
        if os.path.isdir(full_path) and os.path.isdir(os.path.join(full_path, ".git")):
            repos.append(entry)
    return repos

def clone_repo(repo_url, dest_path):
    subprocess.run(["git", "clone", repo_url, dest_path])

def pull_repo(repo_path):
    subprocess.run(["git", "-C", repo_path, "pull"])

