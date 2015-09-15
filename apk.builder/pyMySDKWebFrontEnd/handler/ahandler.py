#
# Copyright 2015 leenjewel
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
#

import tornado.web

class AHandler(tornado.web.RequestHandler) :

    layout = None


    def initialize(self, app) :
        self.app = app

    def render(self, template_name, **kwargs) :
        if None == self.layout :
            return tornado.web.RequestHandler.render(self, template_name, **kwargs)
        else :
            kwargs["content"] = self.render_string(template_name, **kwargs)
            return tornado.web.RequestHandler.render(self, "layouts/" + self.layout, **kwargs)



