import os
import logging
import shutil

workspace = os.path.dirname(os.path.realpath(__file__))  # pwd
pjoin = os.path.join

# the directory structure
# Paddle/
#   modelce/
#     tasks
# DEBUG
paddle_path = pjoin(workspace, '..')
#paddle_path = '/chunwei/Paddle'

baseline_repo_url = 'git@github.com:Superjomn/paddle-ce-latest-kpis.git'

baseline_path = pjoin(workspace, 'tasks')

tmp_root = pjoin(workspace, "tmp")

# mongodb config
db_name = "ce"
table_name = "logs"

