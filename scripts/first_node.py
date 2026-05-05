#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from datetime import datetime  # Для работы со временем

class TimePrinter(Node):
    def __init__(self):
        # Имя узла, под которым он будет виден в системе
        super().__init__('time_printer')
        # Создаём таймер, который будет дёргать колбэк каждые 5 секунд (5.0)
        self.timer = self.create_timer(5.0, self.timer_callback)
        self.get_logger().info('Time printer node has been started. Output every 5 seconds.')

    def timer_callback(self):
        # Получаем текущее время
        now = datetime.now()
        # Форматируем строку
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        # Выводим в лог
        self.get_logger().info(f'Current time: {current_time}')

def main(args=None):
    rclpy.init(args=args)
    node = TimePrinter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
