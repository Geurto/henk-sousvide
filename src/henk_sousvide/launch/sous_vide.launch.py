from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='henk_sousvide',
            executable='sous_vide',
            name='sous_vide',
            parameters=[
                {"a": "b"}
            ]
        )
    ])
