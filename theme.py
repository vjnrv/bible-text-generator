import yaml, os
from yaml.loader import SafeLoader

class Theme:
    def __init__(self, name: str) -> None:
        self.name = name
        self.theme_dir = "themes/%s" % (name)
        self.config = self.load_config()
        self.validate_config()

    def load_config(self) -> dict:
        print("loading theme config %s " % (self.theme_dir))

        if not os.path.isfile(self.config_path):
            raise FileNotFoundError("Theme not found: " + self.name)
        
        with open(self.config_path) as f:
            return yaml.load(f, Loader=SafeLoader)
        
    def validate_config(self) -> None:
        if not self.background or not os.path.isfile(self.background):
            raise RuntimeError("[Theme] Background not specified or not found.")
        
        if not self.style:
            raise RuntimeError("[Theme] Style not defined")
        
        # TODO: Validate every style definition

    @property
    def config_path(self) -> str:
        return "%s/config.yml" % (self.theme_dir)

    @property
    def background(self) -> str:
        if self.config['background']:
            return "%s/%s" % (self.theme_dir, self.config['background'])
        
    @property
    def params(self) -> dict:
        if 'params' in self.config:
            return self.config['params']

        return {}

    @property
    def style(self) -> dict:
        return self.config['style']

    def getparam(self, name: str, _default: any) -> any:
        if name in self.params:
            return self.params[name]

        return _default

    def getstyle(self, name: str) -> dict:
        if not self.style[name]:
            raise RuntimeError("[Theme] Style not found: %s" % (name))

        return self.style[name]
    
    def getstylecolor(self, name: str) -> str:
        style = self.getstyle(name)
        
        if not style['color']:
            raise RuntimeError("[Theme] Style color not defined: %s" % (name))

        return "#%s" % (style['color'])
    
    def getstylesize(self, name: str) -> str:
        style = self.getstyle(name)
        
        if not style['size']:
            raise RuntimeError("[Theme] Style size not defined: %s" % (name))

        return style['size']
    
    def getstylefont(self, name: str) -> str:
        style = self.getstyle(name)
        
        if not style['font']:
            raise RuntimeError("[Theme] Style font not defined: %s" % (name))

        return "%s/%s" % (self.theme_dir, style['font'])
