class DailyDoubleCheck:
    def __init__(self):
        pass
    
    def dailyDoubleCheck(self):
        if self.box[self.boxNum].getDailyDoubleID() == self.d_d1:
            pygame.mixer.music.load("dailyDouble.wav")
            image = pygame.image.load("dailyDouble2.jpg")
            pygame.mixer.music.play()
            width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
            x = int((width - 1075) / 2)
            y = int((height - 750) / 2)

            self.screen.fill((14,27,121))
            self.screen.blit(image, (x, y))
            pygame.display.flip()
            pygame.time.delay(4000)

            self.screen.fill((14,27,121))
            message = "Which player will wager on this Daily Double?"
            self.createDailyDoubleMessage(message)

        elif self.doubleJeopardy == True:
            if self.box[self.boxNum].getDailyDoubleID() == self.d_d2:
                            pygame.mixer.music.load("dailyDouble.wav")
            image = pygame.image.load("dailyDouble2.jpg")
            pygame.mixer.music.play()
            width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
            x = int((width - 1075) / 2)
            y = int((height - 750) / 2)

            self.screen.fill((14,27,121))
            self.screen.blit(image, (x, y))
            pygame.display.flip()
            pygame.time.delay(4000)

            self.screen.fill((14,27,121))
            message = "Which player will wager on this Daily Double?"
            self.createDailyDoubleMessage(message)
