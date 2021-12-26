class slack_block_builder:
    """
    Slack Block Builder
    All methods in this lib return a dictionary (json like) compatible with block message syntax for Slack.

    s = slack_block_builder()
    block_msg = [s.header("Good Morning!"),
                 s.context("Daily update"),
                 s.divider(),
                 s.text("Hello, World!"),
     ]
    """
   
    def image(self, image_url, alt_text = "", title = None):
        image = {"type":"image", "image_url":image_url, "alt_text":alt_text}
        if title is not None:
            image.update({"title":title}) 
        return image


    def button(self, button_text, action_id, url=None, value=None, style=None):
        button = {"type": "button",
                  "text": {"type":"plain_text", "text":button_text, "emoji":True},
                  "action_id":action_id}
        if url is not None:
            button.update({"url":url})
        if value is not None:
            button.update({"value":value})  
        if style is not None:
            button.update({"style":style})
        actions = {"type":"actions", "elements":[button]}
        return actions

    def button_red(self, button_text, action_id, url=None, value=None):
        button = {"type": "button",
                  "text": {"type":"plain_text", "text":button_text, "emoji":True},
                  "action_id":action_id,
                  "style":"danger"}
        if url is not None:
            button.update({"url":url})
        if value is not None:
            button.update({"value":value})
        actions = {"type":"actions", "elements":[button]}
        return actions

    def button_green(self, button_text, action_id, url=None, value=None):
        button = {"type": "button",
                  "text": {"type":"plain_text", "text":button_text, "emoji":True},
                  "action_id":action_id,
                  "style":"primary"}
        if url is not None:
            button.update({"url":url})
        if value is not None:
            button.update({"value":value})
        actions = {"type":"actions", "elements":[button]}
        return actions

    def text(self, text, accessory=None, mrkdwn=True, emoji=True):
        text_element = {"type":"mrkdwn", "text":text} if mrkdwn else\
            {"type":"plain_text", "text":text, "emoji":emoji}
        section = {"type":"section", "text":text_element}
        if type(accessory)==dict:
            if accessory["type"]=="image":
                accessory.update({"title":""})
                image = accessory.pop("title")
                section.update({"accessory":accessory})
            elif accessory["type"]=="actions":
                buttons = accessory["elements"]
                section.update({"accessory":buttons[0]})
        return section

    def context(self, contexts):
        context = {"type":"context"}
        if type(contexts) in [str, dict]:
            contexts = [contexts]
                    
        context["elements"] = [{"type":"mrkdwn", "text":context} if type(context)==str else context for context in contexts]
        return context

    def header(self, header_text, emoji=True):
        return {"type":"header", "text": { "type":"plain_text" ,"text":header_text, "emoji":emoji} }
    
    def divider(self):
        return {"type":"divider"}

    def text_array(self, text_list, mrkdwn=True, emoji=True):
        section = {"type":"section", "fields": [{"type":"mrkdwn", "text": text} if mrkdwn else {"type":"plain_text", "text": text, "emoji":emoji}  for text in text_list] }
        return section
        
    def button_array(self, button_list):
        buttons = [action["elements"][0] for action in button_list]
        actions = {"type":"actions", "elements":buttons}
        return actions
