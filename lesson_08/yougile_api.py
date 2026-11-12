import requests


class YougileProjectsApi:
    def __init__(self, base_url: str, token: str):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, payload: dict):
        return requests.post(
            f"{self.base_url}/api-v2/projects",
            json=payload,
            headers=self.headers
        )

    def get_project(self, project_id: str):
        return requests.get(
            f"{self.base_url}/api-v2/projects/{project_id}",
            headers=self.headers
        )

    def update_project(self, project_id: str, payload: dict):
        return requests.put(
            f"{self.base_url}/api-v2/projects/{project_id}",
            json=payload,
            headers=self.headers
        )
