
def custom_hdr_info(header_rules):
    def hdr_info(span, page=None):
        size = span["size"]
        font = span.get("font", "").lower()
        flags = span.get("flags", 0)
        is_bold = "bold" in font or (flags & 2) != 0
        is_italic = "italic" in font or (flags & 1) != 0

        for rule in header_rules:
            min_is_given = rule.get("min_size") is None or size >= rule["min_size"]
            max_is_given = rule.get("max_size") is None or size < rule["max_size"]
            font_type = rule.get("font")
            font_is_given = font_type is None or \
                            (font_type == "bold" and is_bold) or \
                            (font_type == "italic" and is_italic)
            if min_is_given and max_is_given and font_is_given:
                return rule["level"] + " " if rule["level"] else ""
        return ""
    return hdr_info