def format_mesasge(data):
    messages = []

    for d in data:
        title = d["title"]
        grades = d["grades"]
        
        title = "📌 " + title + "\n" + "♦️ " + grades["total"] + "\n\n" 
        scores = ""

        for p in grades["parts"]:
            part_append = "🟢 " + p["name"] + "\n"
            scores += part_append

            for c in p["containers"]:
                container_append = "🔵 " + c["name"] + ":" + "\n"
                scores += container_append
                for i in c["items"]:
                    item_append =  "⚫️ " + i + "\n"
                    scores += item_append
            scores += "\n"

        msg = title + scores
        messages.append(msg)
        
    return messages