{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sfbllgrn/DD2412_Class_Contrastive_Explanations/blob/main/our_module.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!git clone https://github.com/sfbllgrn/DD2412_Class_Contrastive_Explanations.git\n",
        "\n",
        "import os\n",
        "import shutil\n",
        "\n",
        "# Define the source and destination paths\n",
        "source_folder = '/content/DD2412_Class_Contrastive_Explanations'\n",
        "destination_folder = '/content'\n",
        "\n",
        "# List the files and subdirectories in the source folder\n",
        "contents = os.listdir(source_folder)\n",
        "\n",
        "# Move each item from the source folder to the destination folder\n",
        "for item in contents:\n",
        "    source_path = os.path.join(source_folder, item)\n",
        "    destination_path = os.path.join(destination_folder, item)\n",
        "    shutil.move(source_path, destination_path)\n",
        "\n",
        "# Remove the now-empty source folder\n",
        "os.rmdir(source_folder)\n"
      ],
      "metadata": {
        "id": "QyJVkIHJo4fY",
        "outputId": "a4be7536-c405-4c50-f570-35d7f15cdf9a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'DD2412_Class_Contrastive_Explanations'...\n",
            "remote: Enumerating objects: 33, done.\u001b[K\n",
            "remote: Counting objects: 100% (33/33), done.\u001b[K\n",
            "remote: Compressing objects: 100% (26/26), done.\u001b[K\n",
            "remote: Total 33 (delta 10), reused 15 (delta 1), pack-reused 0\u001b[K\n",
            "Receiving objects: 100% (33/33), 6.09 KiB | 271.00 KiB/s, done.\n",
            "Resolving deltas: 100% (10/10), done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "_c_lwZYNjSAo",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "fb27eaeb-ec28-447c-d26a-d1e838f0a66f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hej\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "2"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ],
      "source": [
        "print(\"hej\")\n",
        "\n",
        "from test_module import my_func\n",
        "\n",
        "\n",
        "my_func()\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "interpreter": {
      "hash": "b2f5f294937e1f47dd6e010afb2ca0c96836afcb29d9a31a278c78890f03e991"
    },
    "kernelspec": {
      "display_name": "Python 3.7.16 64-bit",
      "name": "python3"
    },
    "language_info": {
      "name": "python",
      "version": ""
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}