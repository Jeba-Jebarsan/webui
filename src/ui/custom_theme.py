from gradio.themes import Base
from gradio.themes.utils import colors, sizes

class CustomTheme(Base):
    def __init__(self):
        super().__init__(
            primary_hue=colors.indigo,
            secondary_hue=colors.purple,
            neutral_hue=colors.slate,
            spacing_size=sizes.spacing_lg,
            radius_size=sizes.radius_lg,
            text_size=sizes.text_lg,
        )

        # Custom styles
        self.body_background_fill = "#f8fafc"
        self.block_background_fill = "white"
        self.block_border_width = "0px"
        self.block_shadow = "0 4px 12px rgba(0,0,0,0.05)"
        self.block_radius = "16px"
        
        # Tab styles
        self.tab_selected_background_fill = "linear-gradient(135deg, *primary_100, *secondary_100)"
        self.tab_selected_text_color = "*primary_600"
        self.tab_selected_border_color = "*primary_500"
        self.tab_active_background_fill = "white"
        self.tab_inactive_background_fill = "*neutral_50"
        self.tab_inactive_text_color = "*neutral_700"
        
        # Group styles
        self.group_background_fill = "white"
        self.group_border_color = "*neutral_100"
        self.group_border_width = "1px"
        self.group_border_radius = "12px"
        
        # Button styles
        self.button_primary_background_fill = "linear-gradient(135deg, *primary_500, *secondary_500)"
        self.button_primary_background_fill_hover = "linear-gradient(135deg, *primary_600, *secondary_600)"
        self.button_primary_text_color = "white"
        self.button_primary_border_width = "0"
        self.button_primary_shadow = "0 4px 6px rgba(0,0,0,0.1)"
        
        # Input styles
        self.input_background_fill = "*neutral_50"
        self.input_border_color = "*neutral_200"
        self.input_border_width = "1px"
        self.input_radius = "8px"
        self.input_shadow = "0 2px 4px rgba(0,0,0,0.05)"
        
        # Text styles
        self.font = "Inter, system-ui, sans-serif"