from setuptools import setup

setup(
    name='Rally',
    options={
        'build_apps': {
            # Build Rally.exe as a GUI application
            'gui_apps': {
                'Rally': 'main.py',
            },

            # Set up output logging, important for GUI apps!
            'log_filename': '$USER_APPDATA/Rally/output.log',
            'log_append': False,

            # Files to include
            'include_patterns': [
                'assets/**',
                'highscore/**',
                'tracks/**',
                'UrsinaAchievements/**',

                '**/*.jpg',
                '**/*.png',
                '**/*.obj',
                '**/*.ttf',
                '**/*.wav',
                '**/*.mp3',
                '**/*.ogg',
            ],

            # Files to exclude
            'exclude_patterns': [
                'venv/**',
                'venv313/**',
                'mtl/**',
                '__pycache__/**',
                '.github/**',
                '**/__pycache__/**',
                '**/*.pyc',
                "**/*.mtl",
                "**/*.md",
            ],

            'include_modules': {
                '*': ['ursina']
            },

            # Include the OpenGL renderer and OpenAL audio plug-in
            'plugins': [
                'pandagl',
                'p3openal_audio',
            ],

            "platforms": [
                "win_amd64",
            ],

            "icons": {
                # The key needs to match the key used in gui_apps/console_apps.
                # Alternatively, use "*" to set the icon for all apps.
                "Rally": ["panda3d-logo.png"],
            },
        }
    }
)
