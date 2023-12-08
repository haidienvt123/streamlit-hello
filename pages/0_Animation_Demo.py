# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any

import numpy as np

import streamlit as st
from streamlit.hello.utils import show_code
from flask import Flask


def animation_demo():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        """Example Hello World route."""
        name = os.environ.get("NAME", "World")
        return f"Hello {name}!"

        return data

    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


st.set_page_config(page_title="Animation Demo", page_icon="📹")

animation_demo()
