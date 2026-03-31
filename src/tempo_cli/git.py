import subprocess


# will return HEAD for repos not on github yet, because detached, so assume we created with default
def get_branch_from_git_repo(repo_directory: str) -> str:
    try:
        result = subprocess.run(
            ["git", "-C", repo_directory, "rev-parse", "--abbrev-ref", "HEAD"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )
        if result.stdout.strip() == "HEAD":
            return "master"
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return ""
