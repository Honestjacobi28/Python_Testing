# from locust import HttpUser, task

# class HelloWorldUser(HttpUser):
#     @task
#     def hello_world(self):
#         self.client.get("/showSummary")
#         self.client.get("/purchasePlaces")


from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def submit_form(self):
        form_data = {
            'email': 'john@simplylift.co'
        }
        self.client.post("/showSummary", data=form_data)
