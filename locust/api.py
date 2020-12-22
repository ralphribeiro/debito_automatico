import random
import string

# from locust.contrib.fasthttp import FastHttpUser
from locust import HttpUser, task, between


# base_url = "http://localhost:8000/api/v1"

su_login_data = {"username": "superuser@admin.com",
                 "password": "superuserpassword"}


def random_lower_string(k: int = 32) -> str:
    return "".join(random.choices(string.ascii_lowercase, k=k))


def random_email() -> str:
    return f"{random_lower_string()}@{random_lower_string(10)}.com"


class ApiUser(HttpUser):
    # host = base_url
    wait_time = between(0.5, 5)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nu_id = int()
        self.nu_token = ""

        # get super user token
        with self.client.post("/login/access-token", data=su_login_data) as r:
            self.su_token = r.json()["access_token"]

    def on_start(self):

        user = random_email()
        key = random_lower_string()

        # create new user given email and key
        r = self.client.post(
            "/users/",
            headers={"Authorization": f"Bearer {self.su_token}"},
            json={"email": user, "password": key}
        )
        self.nu_id = r.json()["id"]

        # get new user token
        r = self.client.post(
            "/login/access-token",
            data={"username": user, "password": key}
        )
        self.nu_token = r.json()["access_token"]

        # request automatic debit to new user
        r = self.client.get(
            "/debits/request",
            headers={"Authorization": f"Bearer {self.nu_token}"}
        )

        # change new user automatic debit status by owner_id with super user
        r = self.client.put(f"/debits/{self.nu_id}?status=approved",
                            headers={"Authorization": f"Bearer {self.su_token}"})

    @task
    def get_root(self):
        self.client.get("/")

    @task
    def get_debit(self):
        self.client.get(f"/debits/{self.nu_id}",
                        headers={"Authorization": f"Bearer {self.su_token}"})

    @task
    def get_debit(self):
        self.client.get(f"/debits/{self.nu_id}",
                        headers={"Authorization": f"Bearer {self.nu_token}"})
