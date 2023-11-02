import time, pygame


class Cloud:
    def __init__(self, k):
        self.cloud1_img = pygame.image.load('Data_files/images/clouds/cloud_1.png')
        self.cloud2_img = pygame.image.load('Data_files/images/clouds/cloud_2.png')
        self.cloud1_img = pygame.transform.scale(self.cloud1_img, (220, 80))
        self.cloud2_img = pygame.transform.scale(self.cloud2_img, (220, 80))
        self.animate_cloud = [self.cloud1_img, self.cloud2_img]
        self.current_cloud = self.animate_cloud[k]

    def cloud(self, screen, n, k):
        screen(self.current_cloud, (100, 100))
        screen(self.current_cloud, (800, 150))
        if n == 15:
            self.current_cloud = self.animate_cloud[k]