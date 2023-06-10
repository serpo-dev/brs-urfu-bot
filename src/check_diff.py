import json
import config
import os


def check_diff(subjects):
    diff_grades = []
    is_err = False

    try:
        print("refresh")
        with open(str(config.Config.APP_DIR) + "/cache/" + "cache.json", encoding="utf-8") as f:
            cache = json.load(f)

            for s in subjects:
                if s["title"] not in [x["title"] for x in cache]:
                    diff_grades.append(s)
                else:
                    subject_grades_diff = {"total": s["grades"]["total"], "parts": []}
                    is_subject_diffs = False

                    cached_subject = [x for x in cache if s["title"] == x["title"]][0]

                    for p in s["grades"]["parts"]:
                        if p["name"] not in [x["name"] for x in cached_subject["grades"]["parts"]]:
                            is_subject_diffs = True
                            subject_grades_diff["parts"].append(p)
                            

                    if (is_subject_diffs):
                        diff_grades.append({"id": s["id"], "title": s["title"], "grades": subject_grades_diff})
    
    except Exception as err:
        print(err)
        is_err = True
    finally:
        if len(diff_grades) > 0 or is_err:
            os.makedirs(config.Config.APP_DIR +"/cache", exist_ok=True)
            with open(str(config.Config.APP_DIR) + "/cache/" + "cache.json", "w", encoding="utf-8") as f:
                f.write(json.dumps(subjects, ensure_ascii=False))
                f.close()
            return True, diff_grades
        else:
            return False, None