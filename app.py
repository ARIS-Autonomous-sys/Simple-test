import arcade

# 게임 창의 너비와 높이를 설정
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


# MyGame 클래스는 arcade.Window 클래스를 상속받아 게임 루프를 완벽히 숨깁니다.
class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "2026 모던 2D 게임")
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        """매 프레임 화면을 그리는 렌더링 함수"""
        self.clear()  # 화면 초기화
        arcade.draw_circle_filled(300, 300, 50, arcade.color.BLUE)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()  # 내부적으로 무한 루프가 돕니다.


if __name__ == "__main__":
    main()
