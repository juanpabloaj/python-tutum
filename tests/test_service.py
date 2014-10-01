import unittest
import mock
import tutum

from fake_api import *


class ServiceTestCase(unittest.TestCase):
    @mock.patch.object(tutum.api.http.Session, 'send')
    def test_service_list(self, mock_send):
        attributes = json.loads(
            '[{"autodestroy": "OFF", "autoreplace": "OFF", "autorestart": "OFF", "container_ports": [{"endpoint_uri": null, "inner_port": 80, "outer_port": null, "port_name": "http", "protocol": "tcp", "uri_protocol": "http"}], "cpu_shares": null, "current_num_containers": 3, "deployed_datetime": "Tue, 30 Sep 2014 16:07:36 +0000", "destroyed_datetime": null, "entrypoint": "", "image_name": "tutum/hello-world:latest", "image_tag": "/api/v1/image/tutum/hello-world/tag/latest/", "memory": null, "memory_swap": null, "name": "hello-world", "resource_uri": "/api/v1/service/a2ac25c9-7cfe-4a1b-9d97-66de23642ee8/", "run_command": "/run.sh", "running_num_containers": 3, "sequential_deployment": false, "started_datetime": "Tue, 30 Sep 2014 16:07:36 +0000", "state": "Running", "stopped_datetime": null, "stopped_num_containers": 0, "target_num_containers": 3, "unique_name": "hello-world", "uuid": "a2ac25c9-7cfe-4a1b-9d97-66de23642ee8"}]'
        )
        mock_send.return_value = fake_resp(fake_service_list)
        services = tutum.Service.list()
        for i in range(0, len(services)):
            result = json.loads(json.dumps(services[i].get_all_attributes()))
            target = json.loads(json.dumps(attributes[i]))
            self.assertDictEqual(target, result)

    @mock.patch.object(tutum.api.http.Session, 'send')
    def test_service_fetch(self, mock_send):
        attribute = json.loads(
            '{"actions": ["/api/v1/action/e3ee01df-9f2f-4720-a114-ea1a236d47d2/", "/api/v1/action/c58213ab-8d5c-4a6d-b4c3-bd7157242dc2/"], "autodestroy": "OFF", "autoreplace": "OFF", "autorestart": "OFF", "container_envvars": [], "container_ports": [{"endpoint_uri": null, "inner_port": 80, "outer_port": null, "port_name": "http", "protocol": "tcp", "uri_protocol": "http"}], "containers": ["/api/v1/container/cff4dfa7-28a5-4599-a3f9-c7dc39353c11/", "/api/v1/container/4d966087-5169-4a0b-a2f0-78bbb878d872/", "/api/v1/container/0c84cd78-c239-40ad-939e-dbbc372ae345/"], "cpu_shares": null, "current_num_containers": 3, "deployed_datetime": "Tue, 30 Sep 2014 16:07:36 +0000", "destroyed_datetime": null, "entrypoint": "", "image_name": "tutum/hello-world:latest", "image_tag": "/api/v1/image/tutum/hello-world/tag/latest/", "link_variables": {"HELLO_WORLD_1_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_1_ENV_HOME": "/", "HELLO_WORLD_1_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_1_PORT": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_1_PORT_80_TCP": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_1_PORT_80_TCP_ADDR": "hello-world-1.fa9df19a-tifayuki.node.tutum.io", "HELLO_WORLD_1_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_1_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_2_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_2_ENV_HOME": "/", "HELLO_WORLD_2_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_2_PORT": "tcp://hello-world-2.a2f5a2e9-tifayuki.node.tutum.io:49155", "HELLO_WORLD_2_PORT_80_TCP": "tcp://hello-world-2.a2f5a2e9-tifayuki.node.tutum.io:49155", "HELLO_WORLD_2_PORT_80_TCP_ADDR": "hello-world-2.a2f5a2e9-tifayuki.node.tutum.io", "HELLO_WORLD_2_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_2_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_3_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_3_ENV_HOME": "/", "HELLO_WORLD_3_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_3_PORT": "tcp://hello-world-3.5067d4f4-tifayuki.node.tutum.io:49155", "HELLO_WORLD_3_PORT_80_TCP": "tcp://hello-world-3.5067d4f4-tifayuki.node.tutum.io:49155", "HELLO_WORLD_3_PORT_80_TCP_ADDR": "hello-world-3.5067d4f4-tifayuki.node.tutum.io", "HELLO_WORLD_3_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_3_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_ENV_HOME": "/", "HELLO_WORLD_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_PORT": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_PORT_80_TCP": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_PORT_80_TCP_ADDR": "hello-world-1.fa9df19a-tifayuki.node.tutum.io", "HELLO_WORLD_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_TUTUM_API_URL": "https://dashboard.tutum.co/api/v1/service/a2ac25c9-7cfe-4a1b-9d97-66de23642ee8/"}, "linked_from_service": [], "linked_to_service": [], "memory": null, "memory_swap": null, "name": "hello-world", "resource_uri": "/api/v1/service/a2ac25c9-7cfe-4a1b-9d97-66de23642ee8/", "roles": [], "run_command": "/run.sh", "running_num_containers": 3, "sequential_deployment": false, "started_datetime": "Tue, 30 Sep 2014 16:07:36 +0000", "state": "Running", "stopped_datetime": null, "stopped_num_containers": 0, "target_num_containers": 3, "unique_name": "hello-world", "uuid": "a2ac25c9-7cfe-4a1b-9d97-66de23642ee8"}')
        mock_send.return_value = fake_resp(fake_service_fetch)
        service = tutum.Service.fetch('a2ac25c9-7cfe-4a1b-9d97-66de23642ee8')
        result = json.loads(json.dumps(service.get_all_attributes()))
        target = json.loads(json.dumps(attribute))
        self.assertDictEqual(target, result)

    @mock.patch.object(tutum.api.http.Session, 'send')
    def test_service_save(self, mock_send):
        attribute = json.loads(
            '{"actions": ["/api/v1/action/e3ee01df-9f2f-4720-a114-ea1a236d47d2/", "/api/v1/action/c58213ab-8d5c-4a6d-b4c3-bd7157242dc2/", "/api/v1/action/b3adfa79-dbd2-41a4-8c71-5e242ecce9bb/", "/api/v1/action/f82e25e7-d550-454e-a897-8599f2f530e5/"], "autodestroy": "OFF", "autoreplace": "OFF", "autorestart": "OFF", "container_envvars": [], "container_ports": [{"endpoint_uri": null, "inner_port": 80, "outer_port": null, "port_name": "http", "protocol": "tcp", "uri_protocol": "http"}], "containers": ["/api/v1/container/cff4dfa7-28a5-4599-a3f9-c7dc39353c11/", "/api/v1/container/4d966087-5169-4a0b-a2f0-78bbb878d872/", "/api/v1/container/0c84cd78-c239-40ad-939e-dbbc372ae345/"], "cpu_shares": null, "current_num_containers": 3, "deployed_datetime": "Tue, 30 Sep 2014 16:07:36 +0000", "destroyed_datetime": null, "entrypoint": "", "image_name": "tutum/hello-world:latest", "image_tag": "/api/v1/image/tutum/hello-world/tag/latest/", "link_variables": {"HELLO_WORLD_1_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_1_ENV_HOME": "/", "HELLO_WORLD_1_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_1_PORT": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_1_PORT_80_TCP": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_1_PORT_80_TCP_ADDR": "hello-world-1.fa9df19a-tifayuki.node.tutum.io", "HELLO_WORLD_1_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_1_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_2_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_2_ENV_HOME": "/", "HELLO_WORLD_2_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_2_PORT": "tcp://hello-world-2.a2f5a2e9-tifayuki.node.tutum.io:49155", "HELLO_WORLD_2_PORT_80_TCP": "tcp://hello-world-2.a2f5a2e9-tifayuki.node.tutum.io:49155", "HELLO_WORLD_2_PORT_80_TCP_ADDR": "hello-world-2.a2f5a2e9-tifayuki.node.tutum.io", "HELLO_WORLD_2_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_2_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_3_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_3_ENV_HOME": "/", "HELLO_WORLD_3_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_3_PORT": "tcp://hello-world-3.5067d4f4-tifayuki.node.tutum.io:49155", "HELLO_WORLD_3_PORT_80_TCP": "tcp://hello-world-3.5067d4f4-tifayuki.node.tutum.io:49155", "HELLO_WORLD_3_PORT_80_TCP_ADDR": "hello-world-3.5067d4f4-tifayuki.node.tutum.io", "HELLO_WORLD_3_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_3_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_ENV_HOME": "/", "HELLO_WORLD_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_PORT": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_PORT_80_TCP": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_PORT_80_TCP_ADDR": "hello-world-1.fa9df19a-tifayuki.node.tutum.io", "HELLO_WORLD_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_TUTUM_API_URL": "https://dashboard.tutum.co/api/v1/service/a2ac25c9-7cfe-4a1b-9d97-66de23642ee8/"}, "linked_from_service": [], "linked_to_service": [], "memory": null, "memory_swap": null, "name": "hello-world", "resource_uri": "/api/v1/service/a2ac25c9-7cfe-4a1b-9d97-66de23642ee8/", "roles": [], "run_command": "/run.sh", "running_num_containers": 3, "sequential_deployment": false, "started_datetime": "Tue, 30 Sep 2014 16:07:36 +0000", "state": "Scaling", "stopped_datetime": null, "stopped_num_containers": 0, "target_num_containers": 5, "unique_name": "hello-world", "uuid": "a2ac25c9-7cfe-4a1b-9d97-66de23642ee8", "web_public_dns": ""}'
        )
        mock_send.side_effect = [fake_resp(fake_service_fetch), fake_resp(fake_service_save)]
        service = tutum.Service.fetch('a2ac25c9-7cfe-4a1b-9d97-66de23642ee8')
        service.target_num_containers = 5
        self.assertTrue(service.save())
        result = json.loads(json.dumps(service.get_all_attributes()))
        target = json.loads(json.dumps(attribute))
        self.assertDictEqual(target, result)

    @mock.patch.object(tutum.api.http.Session, 'send')
    def test_service_delete(self, mock_send):
        attribute = json.loads(
            '{"actions": ["/api/v1/action/e3ee01df-9f2f-4720-a114-ea1a236d47d2/", "/api/v1/action/c58213ab-8d5c-4a6d-b4c3-bd7157242dc2/", "/api/v1/action/b3adfa79-dbd2-41a4-8c71-5e242ecce9bb/", "/api/v1/action/f82e25e7-d550-454e-a897-8599f2f530e5/", "/api/v1/action/381c53a0-bf18-4a01-a1b0-be87051c35e8/"], "autodestroy": "OFF", "autoreplace": "OFF", "autorestart": "OFF", "container_envvars": [], "container_ports": [{"endpoint_uri": null, "inner_port": 80, "outer_port": null, "port_name": "http", "protocol": "tcp", "uri_protocol": "http"}], "containers": ["/api/v1/container/cff4dfa7-28a5-4599-a3f9-c7dc39353c11/", "/api/v1/container/4d966087-5169-4a0b-a2f0-78bbb878d872/", "/api/v1/container/0c84cd78-c239-40ad-939e-dbbc372ae345/", "/api/v1/container/6e74df59-83ee-4351-8ba9-3d26e0d64c34/", "/api/v1/container/7bbff9f0-af41-408f-9dd0-213cd67e4aa2/"], "cpu_shares": null, "current_num_containers": 5, "deployed_datetime": "Tue, 30 Sep 2014 16:07:36 +0000", "destroyed_datetime": null, "entrypoint": "", "image_name": "tutum/hello-world:latest", "image_tag": "/api/v1/image/tutum/hello-world/tag/latest/", "link_variables": {"HELLO_WORLD_1_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_1_ENV_HOME": "/", "HELLO_WORLD_1_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_1_PORT": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_1_PORT_80_TCP": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_1_PORT_80_TCP_ADDR": "hello-world-1.fa9df19a-tifayuki.node.tutum.io", "HELLO_WORLD_1_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_1_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_2_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_2_ENV_HOME": "/", "HELLO_WORLD_2_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_2_PORT": "tcp://hello-world-2.a2f5a2e9-tifayuki.node.tutum.io:49155", "HELLO_WORLD_2_PORT_80_TCP": "tcp://hello-world-2.a2f5a2e9-tifayuki.node.tutum.io:49155", "HELLO_WORLD_2_PORT_80_TCP_ADDR": "hello-world-2.a2f5a2e9-tifayuki.node.tutum.io", "HELLO_WORLD_2_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_2_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_3_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_3_ENV_HOME": "/", "HELLO_WORLD_3_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_3_PORT": "tcp://hello-world-3.5067d4f4-tifayuki.node.tutum.io:49155", "HELLO_WORLD_3_PORT_80_TCP": "tcp://hello-world-3.5067d4f4-tifayuki.node.tutum.io:49155", "HELLO_WORLD_3_PORT_80_TCP_ADDR": "hello-world-3.5067d4f4-tifayuki.node.tutum.io", "HELLO_WORLD_3_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_3_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_4_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_4_ENV_HOME": "/", "HELLO_WORLD_4_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_4_PORT": "tcp://hello-world-4.5067d4f4-tifayuki.node.tutum.io:49156", "HELLO_WORLD_4_PORT_80_TCP": "tcp://hello-world-4.5067d4f4-tifayuki.node.tutum.io:49156", "HELLO_WORLD_4_PORT_80_TCP_ADDR": "hello-world-4.5067d4f4-tifayuki.node.tutum.io", "HELLO_WORLD_4_PORT_80_TCP_PORT": "49156", "HELLO_WORLD_4_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_5_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_5_ENV_HOME": "/", "HELLO_WORLD_5_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_5_PORT": "tcp://hello-world-5.fa9df19a-tifayuki.node.tutum.io:49157", "HELLO_WORLD_5_PORT_80_TCP": "tcp://hello-world-5.fa9df19a-tifayuki.node.tutum.io:49157", "HELLO_WORLD_5_PORT_80_TCP_ADDR": "hello-world-5.fa9df19a-tifayuki.node.tutum.io", "HELLO_WORLD_5_PORT_80_TCP_PORT": "49157", "HELLO_WORLD_5_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_ENV_DEBIAN_FRONTEND": "noninteractive", "HELLO_WORLD_ENV_HOME": "/", "HELLO_WORLD_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "HELLO_WORLD_PORT": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_PORT_80_TCP": "tcp://hello-world-1.fa9df19a-tifayuki.node.tutum.io:49155", "HELLO_WORLD_PORT_80_TCP_ADDR": "hello-world-1.fa9df19a-t* Connection #0 to host dashboard.tutum.co left intactifayuki.node.tutum.io", "HELLO_WORLD_PORT_80_TCP_PORT": "49155", "HELLO_WORLD_PORT_80_TCP_PROTO": "tcp", "HELLO_WORLD_TUTUM_API_URL": "https://dashboard.tutum.co/api/v1/service/a2ac25c9-7cfe-4a1b-9d97-66de23642ee8/"}, "linked_from_service": [], "linked_to_service": [], "memory": null, "memory_swap": null, "name": "hello-world", "resource_uri": "/api/v1/service/a2ac25c9-7cfe-4a1b-9d97-66de23642ee8/", "roles": [], "run_command": "/run.sh", "running_num_containers": 3, "sequential_deployment": false, "started_datetime": "Tue, 30 Sep 2014 22:57:36 +0000", "state": "Terminating", "stopped_datetime": null, "stopped_num_containers": 0, "target_num_containers": 0, "unique_name": "hello-world", "uuid": "a2ac25c9-7cfe-4a1b-9d97-66de23642ee8"}'
        )
        mock_send.side_effect = [fake_resp(fake_service_fetch), fake_resp(fake_service_delete)]
        service = tutum.Service.fetch('a2ac25c9-7cfe-4a1b-9d97-66de23642ee8')
        self.assertTrue(service.delete())
        result = json.loads(json.dumps(service.get_all_attributes()))
        target = json.loads(json.dumps(attribute))
        self.assertDictEqual(target, result)

    @mock.patch.object(tutum.api.http.Session, 'send')
    def test_service_logs(self, mock_send):
        target = "[mysql-1] 2014-09-30T22:44:31.385643366Z => An empty or uninitialized MySQL volume is detected in /var/lib/mysql\n[mysql-1] 2014-09-30T22:44:31.386200239Z => Installing MySQL ...\n"
        mock_send.side_effect = [fake_resp(fake_service_fetch), fake_resp(fake_service_logs)]
        service = tutum.Service.fetch('5ecde92d-498b-4bbb-b773-a998e5e421dc')
        self.assertEqual(target, service.logs)

    @mock.patch.object(tutum.api.http.Session, 'send')
    def test_service_start(self, mock_send):
        attribute = json.loads(
            '{"actions": ["/api/v1/action/a8aaf64b-3186-41e7-9256-6b3d69786036/", "/api/v1/action/2481790d-a860-4bb4-95d2-5676ae2d6748/", "/api/v1/action/799a0d06-efae-4bf1-b063-7141f722cbb1/", "/api/v1/action/ef6b9f59-1edb-44c7-bcc6-1b80f737e4b0/", "/api/v1/action/99b7ac29-d16d-448f-bac5-54dbd5dd3b7b/"], "autodestroy": "OFF", "autoreplace": "OFF", "autorestart": "OFF", "container_envvars": [], "container_ports": [{"endpoint_uri": null, "inner_port": 3306, "outer_port": null, "port_name": "mysql", "protocol": "tcp", "uri_protocol": "mysql"}], "containers": ["/api/v1/container/2a1c4057-7753-4393-98c6-35699c198e08/", "/api/v1/container/54ead360-698f-4354-96f7-538f686cdd69/"], "cpu_shares": null, "current_num_containers": 2, "deployed_datetime": "Tue, 30 Sep 2014 22:44:44 +0000", "destroyed_datetime": null, "entrypoint": "", "image_name": "tutum/mysql:latest", "image_tag": "/api/v1/image/tutum/mysql/tag/latest/", "link_variables": {"MYSQL_TUTUM_API_URL": "https://dashboard.tutum.co/api/v1/service/5ecde92d-498b-4bbb-b773-a998e5e421dc/"}, "linked_from_service": [], "linked_to_service": [], "memory": null, "memory_swap": null, "name": "mysql", "resource_uri": "/api/v1/service/5ecde92d-498b-4bbb-b773-a998e5e421dc/", "roles": [], "run_command": "/run.sh", "running_num_containers": 0, "sequential_deployment": false, "started_datetime": "Tue, 30 Sep 2014 22:44:44 +0000", "state": "Starting", "stopped_datetime": "Tue, 30 Sep 2014 23:09:09 +0000", "stopped_num_containers": 2, "target_num_containers": 2, "unique_name": "mysql", "uuid": "5ecde92d-498b-4bbb-b773-a998e5e421dc"}'
        )
        mock_send.side_effect = [fake_resp(fake_service_fetch), fake_resp(fake_service_start)]
        service = tutum.Service.fetch('a2ac25c9-7cfe-4a1b-9d97-66de23642ee8')
        self.assertTrue(service.start())
        result = json.loads(json.dumps(service.get_all_attributes()))
        target = json.loads(json.dumps(attribute))
        self.assertDictEqual(target, result)

    @mock.patch.object(tutum.api.http.Session, 'send')
    def test_service_stop(self, mock_send):
        attribute = json.loads(
            '{"actions": ["/api/v1/action/a8aaf64b-3186-41e7-9256-6b3d69786036/", "/api/v1/action/2481790d-a860-4bb4-95d2-5676ae2d6748/", "/api/v1/action/799a0d06-efae-4bf1-b063-7141f722cbb1/", "/api/v1/action/ef6b9f59-1edb-44c7-bcc6-1b80f737e4b0/", "/api/v1/action/99b7ac29-d16d-448f-bac5-54dbd5dd3b7b/", "/api/v1/action/98816bfc-4fa7-4697-bea1-d926de69b48f/"], "autodestroy": "OFF", "autoreplace": "OFF", "autorestart": "OFF", "container_envvars": [], "container_ports": [{"endpoint_uri": null, "inner_port": 3306, "outer_port": null, "port_name": "mysql", "protocol": "tcp", "uri_protocol": "mysql"}], "containers": ["/api/v1/container/2a1c4057-7753-4393-98c6-35699c198e08/", "/api/v1/container/54ead360-698f-4354-96f7-538f686cdd69/"], "cpu_shares": null, "current_num_containers": 2, "deployed_datetime": "Tue, 30 Sep 2014 22:44:44 +0000", "destroyed_datetime": null, "entrypoint": "", "image_name": "tutum/mysql:latest", "image_tag": "/api/v1/image/tutum/mysql/tag/latest/", "link_variables": {"MYSQL_1_ENV_DEBIAN_FRONTEND": "noninteractive", "MYSQL_1_ENV_MYSQL_PASS": "**Random**", "MYSQL_1_ENV_MYSQL_USER": "admin", "MYSQL_1_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "MYSQL_1_ENV_REPLICATION_MASTER": "**False**", "MYSQL_1_ENV_REPLICATION_PASS": "replica", "MYSQL_1_ENV_REPLICATION_SLAVE": "**False**", "MYSQL_1_ENV_REPLICATION_USER": "replica", "MYSQL_1_PORT": "tcp://mysql-1.fa9df19a-tifayuki.node.tutum.io:49156", "MYSQL_1_PORT_3306_TCP": "tcp://mysql-1.fa9df19a-tifayuki.node.tutum.io:49156", "MYSQL_1_PORT_3306_TCP_ADDR": "mysql-1.fa9df19a-tifayuki.node.tutum.io", "MYSQL_1_PORT_3306_TCP_PORT": "49156", "MYSQL_1_PORT_3306_TCP_PROTO": "tcp", "MYSQL_2_ENV_DEBIAN_FRONTEND": "noninteractive", "MYSQL_2_ENV_MYSQL_PASS": "**Random**", "MYSQL_2_ENV_MYSQL_USER": "admin", "MYSQL_2_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "MYSQL_2_ENV_REPLICATION_MASTER": "**False**", "MYSQL_2_ENV_REPLICATION_PASS": "replica", "MYSQL_2_ENV_REPLICATION_SLAVE": "**False**", "MYSQL_2_ENV_REPLICATION_USER": "replica", "MYSQL_2_PORT": "tcp://mysql-2.a2f5a2e9-tifayuki.node.tutum.io:49156", "MYSQL_2_PORT_3306_TCP": "tcp://mysql-2.a2f5a2e9-tifayuki.node.tutum.io:49156", "MYSQL_2_PORT_3306_TCP_ADDR": "mysql-2.a2f5a2e9-tifayuki.node.tutum.io", "MYSQL_2_PORT_3306_TCP_PORT": "49156", "MYSQL_2_PORT_3306_TCP_PROTO": "tcp", "MYSQL_ENV_DEBIAN_FRONTEND": "noninteractive", "MYSQL_ENV_MYSQL_PASS": "**Random**", "MYSQL_ENV_MYSQL_USER": "admin", "MYSQL_ENV_PATH": "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin", "MYSQL_ENV_REPLICATION_MASTER": "**False**", "MYSQL_ENV_REPLICATION_PASS": "replica", "MYSQL_ENV_REPLICATION_SLAVE": "**False**", "MYSQL_ENV_REPLICATION_USER": "replica", "MYSQL_PORT": "tcp://mysql-1.fa9df19a-tifayuki.node.tutum.io:49156", "MYSQL_PORT_3306_TCP": "tcp://mysql-1.fa9df19a-tifayuki.node.tutum.io:49156", "MYSQL_PORT_3306_TCP_ADDR": "mysql-1.fa9df19a-tifayuki.node.tutum.io", "MYSQL_PORT_3306_TCP_PORT": "49156", "MYSQL_PORT_3306_TCP_PROTO": "tcp", "MYSQL_TUTUM_API_URL": "https://dashboard.tutum.co/api/v1/service/5ecde92d-498b-4bbb-b773-a998e5e421dc/"}, "linked_from_service": [], "linked_to_service": [], "memory": null, "memory_swap": null, "name": "mysql", "resource_uri": "/api/v1/service/5ecde92d-498b-4bbb-b773-a998e5e421dc/", "roles": [], "run_command": "/run.sh", "running_num_containers": 1, "sequential_deployment": false, "started_datetime": "Tue, 30 Sep 2014 23:50:59 +0000", "state": "Stopping", "stopped_datetime": "Tue, 30 Sep 2014 23:09:09 +0000", "stopped_num_containers": 0, "target_num_containers": 2, "unique_name": "mysql", "uuid": "5ecde92d-498b-4bbb-b773-a998e5e421dc"}'
        )
        mock_send.side_effect = [fake_resp(fake_service_fetch), fake_resp(fake_service_stop)]
        service = tutum.Service.fetch('a2ac25c9-7cfe-4a1b-9d97-66de23642ee8')
        self.assertTrue(service.stop())
        result = json.loads(json.dumps(service.get_all_attributes()))
        target = json.loads(json.dumps(attribute))
        self.assertDictEqual(target, result)

    @mock.patch.object(tutum.api.http.Session, 'send')
    def test_service_redeploy(self, mock_send):
        attribute = json.loads(
            '{"actions": ["/api/v1/action/a8aaf64b-3186-41e7-9256-6b3d69786036/", "/api/v1/action/2481790d-a860-4bb4-95d2-5676ae2d6748/", "/api/v1/action/799a0d06-efae-4bf1-b063-7141f722cbb1/", "/api/v1/action/ef6b9f59-1edb-44c7-bcc6-1b80f737e4b0/", "/api/v1/action/99b7ac29-d16d-448f-bac5-54dbd5dd3b7b/", "/api/v1/action/98816bfc-4fa7-4697-bea1-d926de69b48f/", "/api/v1/action/285e250f-7429-4f0a-a252-5594a05c8020/"], "autodestroy": "OFF", "autoreplace": "OFF", "autorestart": "OFF", "container_envvars": [], "container_ports": [{"endpoint_uri": null, "inner_port": 3306, "outer_port": null, "port_name": "mysql", "protocol": "tcp", "uri_protocol": "mysql"}], "containers": ["/api/v1/container/2a1c4057-7753-4393-98c6-35699c198e08/", "/api/v1/container/54ead360-698f-4354-96f7-538f686cdd69/"], "cpu_shares": null, "current_num_containers": 2, "deployed_datetime": "Tue, 30 Sep 2014 22:44:44 +0000", "destroyed_datetime": null, "entrypoint": "", "image_name": "tutum/mysql:latest", "image_tag": "/api/v1/image/tutum/mysql/tag/latest/", "link_variables": {"MYSQL_TUTUM_API_URL": "https://dashboard.tutum.co/api/v1/service/5ecde92d-498b-4bbb-b773-a998e5e421dc/"}, "linked_from_service": [], "linked_to_service": [], "memory": null, "memory_swap": null, "name": "mysql", "resource_uri": "/api/v1/service/5ecde92d-498b-4bbb-b773-a998e5e421dc/", "roles": [], "run_command": "/run.sh", "running_num_containers": 0, "sequential_deployment": false, "started_datetime": "Tue, 30 Sep 2014 23:50:59 +0000", "state": "Redeploying", "stopped_datetime": "Tue, 30 Sep 2014 23:51:52 +0000", "stopped_num_containers": 0, "target_num_containers": 2, "unique_name": "mysql", "uuid": "5ecde92d-498b-4bbb-b773-a998e5e421dc"}'
        )
        mock_send.side_effect = [fake_resp(fake_service_fetch), fake_resp(fake_service_redeploy)]
        service = tutum.Service.fetch('a2ac25c9-7cfe-4a1b-9d97-66de23642ee8')
        self.assertTrue(service.redeploy())
        result = json.loads(json.dumps(service.get_all_attributes()))
        target = json.loads(json.dumps(attribute))
        self.assertDictEqual(target, result)