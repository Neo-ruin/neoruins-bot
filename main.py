from datetime import datetime
from pathlib import Path
import os
import re

import tweepy
from dotenv import load_dotenv

APPROVED_FILE = Path("approved_posts.txt")
HISTORY_FILE = Path("content_history.txt")
DRAFTS_FILE = Path("drafts.txt")
PERFORMANCE_FILE = Path("performance_history.txt")
PUBLISHED_FILE = Path("published_posts.txt")

MIN_POST_GAP_MINUTES = 60

PERSONALITY = {
    "Name": "NEORUINS",
    "Style": "Casual, confident, conversational, gaming-focused",
    "Tone": "Energetic, authentic, sometimes sarcastic",
    "Goal": "Create posts that encourage replies, reposts, and discussion",
}

POST_TYPE_PURPOSES = {
    "Gaming Question": "Start conversations and encourage people to reply.",
    "Hot Take": "Create discussion around a strong gaming opinion.",
    "News Reaction": "React quickly to gaming news and give people a reason to engage.",
    "Streaming Post": "Promote streams and encourage viewers to join the conversation.",
    "Meme Style": "Create relatable gaming humor that people want to share.",
}

BRAND_VOICE = {
    "Audience": "Gamers, streamers, and gaming communities",
    "Personality": "Authentic, energetic, humorous, and conversational",
    "Writing Style": "Short, punchy, easy to read, and engagement-focused",
    "Avoid": "Overly corporate language, forced engagement, and excessive hashtags",
}

POSTING_TIME_RECOMMENDATIONS = [
    ("12:00 PM", "Midday gaming and social-media activity."),
    ("6:00 PM", "After-work and after-school gaming activity."),
    ("8:00 PM", "Evening gaming and community activity."),
]


def load_lines(file_path):
    if not file_path.exists():
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        return [line.rstrip("\n") for line in file]


def show_personality():
    print("\n--- NEORUINS PERSONALITY ---")
    print(f"Name: {PERSONALITY['Name']}")
    print(f"Style: {PERSONALITY['Style']}")
    print(f"Tone: {PERSONALITY['Tone']}")
    print(f"Goal: {PERSONALITY['Goal']}")


def show_brand_voice():
    print("\n--- BRAND VOICE ---")
    print(f"Audience: {BRAND_VOICE['Audience']}")
    print(f"Personality: {BRAND_VOICE['Personality']}")
    print(f"Writing Style: {BRAND_VOICE['Writing Style']}")
    print(f"Avoid: {BRAND_VOICE['Avoid']}")


def show_posting_time_recommendations():
    print("\n--- POSTING TIME STARTING POINTS ---")

    for time_text, reason in POSTING_TIME_RECOMMENDATIONS:
        print(f"{time_text} - {reason}")

    print("\nThese are starting points for testing, not guarantees.")


def quality_check(post):
    checks = []

    if len(post) <= 280:
        checks.append("PASS: Within 280 characters.")
    else:
        checks.append("WARNING: Over 280 characters.")

    if len(post.split()) >= 5:
        checks.append("PASS: Post has enough text to communicate an idea.")
    else:
        checks.append("WARNING: Post may be too short.")

    if "?" in post:
        checks.append("PASS: Encourages conversation with a question.")
    else:
        checks.append("INFO: No question detected.")

    if "#" in post:
        checks.append("PASS: Contains a hashtag.")
    else:
        checks.append("INFO: No hashtag detected.")

    return checks


def calculate_score(post):
    score = 50

    if "?" in post:
        score += 15

    if len(post) <= 280:
        score += 10

    if "#" in post:
        score += 5

    if any(word in post.lower() for word in ["you", "your", "what", "who", "why"]):
        score += 10

    if len(post.split()) >= 10:
        score += 10

    return min(score, 100)


def content_is_original(post):
    existing_content = []

    for file_path in [APPROVED_FILE, HISTORY_FILE, DRAFTS_FILE]:
        existing_content.extend(load_lines(file_path))

    post_lower = post.strip().lower()

    for line in existing_content:
        if post_lower and post_lower in line.lower():
            return False

    return True


def generate_posts(topic, post_type):
    hashtag = "#Gaming"

    if post_type == "Gaming Question":
        return [
            f"What's one game you could replay forever? 🎮 {topic} {hashtag}",
            f"Gamers, be honest... what's the best thing about {topic}? 👀 {hashtag}",
            f"If you could change ONE thing about {topic}, what would it be? {hashtag}",
        ]

    if post_type == "Hot Take":
        return [
            f"Hot take: {topic} doesn't get nearly enough credit. 🔥 {hashtag}",
            f"I'm probably going to get hate for this... {topic} is underrated. {hashtag}",
            f"Unpopular gaming opinion: {topic} deserves way more attention. 👀 {hashtag}",
        ]

    if post_type == "News Reaction":
        return [
            f"Okay... this {topic} news actually caught me off guard. 👀 {hashtag}",
            f"Not gonna lie, I wasn't expecting this from {topic}. What do you think? {hashtag}",
            f"Gaming news is getting wild. That {topic} update has everyone talking. 🔥 {hashtag}",
        ]

    if post_type == "Streaming Post":
        return [
            f"Going live soon! 🎮 We're jumping into {topic}. Come hang out! {hashtag}",
            f"Stream time! 🔴 Tonight we're playing {topic}. Who's joining? {hashtag}",
            f"Who's ready for some {topic}? Going live soon. 👀🎮 {hashtag}",
        ]

    if post_type == "Meme Style":
        return [
            f"Me: I'll play {topic} for 30 minutes.\nAlso me 4 hours later: 💀 {hashtag}",
            f"POV: You said one more game of {topic}.\nIt's suddenly 3 AM. 💀 {hashtag}",
            f"Nobody:\nAbsolutely nobody:\nMe: \"One more game of {topic}.\" 🎮 {hashtag}",
        ]

    return []


def show_quality_results(post):
    print("\n--- QUALITY CHECK ---")

    for result in quality_check(post):
        print(result)


def save_approved_post(post, topic, post_type, score):
    with open(APPROVED_FILE, "a", encoding="utf-8") as file:
        file.write("\n--- APPROVED POST ---\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Topic: {topic}\n")
        file.write(f"Post Type: {post_type}\n")
        file.write(f"Score: {score}/100\n")
        file.write(f"Post: {post}\n")

    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write("\n--- CONTENT HISTORY ---\n")
        file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Topic: {topic}\n")
        file.write(f"Post Type: {post_type}\n")
        file.write(f"Score: {score}/100\n")
        file.write(f"Post: {post}\n")


def load_drafts():
    drafts = []

    if not DRAFTS_FILE.exists():
        return drafts

    with open(DRAFTS_FILE, "r", encoding="utf-8") as file:
        content = file.read().strip()

    if not content:
        return drafts

    blocks = content.split("\n--- DRAFT ---\n")

    for block in blocks:
        if not block.strip():
            continue

        lines = block.splitlines()

        draft = {
            "date_created": "",
            "scheduled_for": "Not scheduled",
            "topic": "",
            "post_type": "",
            "score": "",
            "post": "",
        }

        for line in lines:
            if line.startswith("Date Created:"):
                draft["date_created"] = line.replace("Date Created:", "", 1).strip()
            elif line.startswith("Scheduled For:"):
                draft["scheduled_for"] = line.replace("Scheduled For:", "", 1).strip()
            elif line.startswith("Topic:"):
                draft["topic"] = line.replace("Topic:", "", 1).strip()
            elif line.startswith("Post Type:"):
                draft["post_type"] = line.replace("Post Type:", "", 1).strip()
            elif line.startswith("Score:"):
                draft["score"] = line.replace("Score:", "", 1).strip()
            elif line.startswith("Post:"):
                draft["post"] = line.replace("Post:", "", 1).strip()

        drafts.append(draft)

    return drafts


def write_drafts(drafts):
    with open(DRAFTS_FILE, "w", encoding="utf-8") as file:
        for draft in drafts:
            file.write("\n--- DRAFT ---\n")
            file.write(f"Date Created: {draft['date_created']}\n")
            file.write(f"Scheduled For: {draft['scheduled_for']}\n")
            file.write(f"Topic: {draft['topic']}\n")
            file.write(f"Post Type: {draft['post_type']}\n")
            file.write(f"Score: {draft['score']}\n")
            file.write(f"Post: {draft['post']}\n")


def parse_schedule(schedule_text):
    try:
        return datetime.strptime(schedule_text, "%Y-%m-%d %H:%M")
    except ValueError:
        return None


def schedule_conflict(schedule_text, drafts, ignore_index=None):
    target_time = parse_schedule(schedule_text)

    if target_time is None:
        return None

    for index, draft in enumerate(drafts):
        if ignore_index is not None and index == ignore_index:
            continue

        existing_time = parse_schedule(draft["scheduled_for"])

        if existing_time and existing_time == target_time:
            return draft

    return None


def frequency_warning(schedule_text, drafts, ignore_index=None):
    target_time = parse_schedule(schedule_text)

    if target_time is None:
        return None

    for index, draft in enumerate(drafts):
        if ignore_index is not None and index == ignore_index:
            continue

        existing_time = parse_schedule(draft["scheduled_for"])

        if existing_time is None:
            continue

        difference = abs((target_time - existing_time).total_seconds()) / 60

        if difference < MIN_POST_GAP_MINUTES:
            return {
                "draft": draft,
                "difference": difference,
            }

    return None


def show_frequency_warning(warning):
    if not warning:
        return

    print("\nWARNING: These scheduled posts are less than")
    print(f"{MIN_POST_GAP_MINUTES} minutes apart.")

    print(f"Existing post: {warning['draft']['topic']}")
    print(f"Scheduled for: {warning['draft']['scheduled_for']}")
    print(f"Time difference: {warning['difference']:.0f} minutes")

    print("\nYou can still continue scheduling this post.")


def valid_future_schedule():
    while True:
        schedule_text = input(
            "\nEnter scheduled date/time (YYYY-MM-DD HH:MM)\n"
            "or press Enter for no schedule: "
        ).strip()

        if not schedule_text:
            return "Not scheduled"

        scheduled_time = parse_schedule(schedule_text)

        if scheduled_time is None:
            print("Invalid format. Please use YYYY-MM-DD HH:MM.")
            continue

        if scheduled_time <= datetime.now():
            print("That time has already passed. Please enter a future time.")
            continue

        return schedule_text


def save_draft(topic, post_type, post, score):
    drafts = load_drafts()
    schedule_text = valid_future_schedule()

    if schedule_text != "Not scheduled":
        conflict = schedule_conflict(schedule_text, drafts)

        if conflict:
            print("\nSCHEDULE CONFLICT DETECTED.")
            print(f"Existing topic: {conflict['topic']}")
            print(f"Existing post type: {conflict['post_type']}")
            print(f"Scheduled for: {conflict['scheduled_for']}")
            print("Draft was NOT saved.")
            return

        warning = frequency_warning(schedule_text, drafts)
        show_frequency_warning(warning)
        show_posting_time_recommendations()

    draft = {
        "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "scheduled_for": schedule_text,
        "topic": topic,
        "post_type": post_type,
        "score": f"{score}/100",
        "post": post,
    }

    drafts.append(draft)
    write_drafts(drafts)

    print("\nDraft saved successfully.")


def review_post(post, topic, post_type, score):
    while True:
        print("\n--- REVIEW POST ---")
        print(post)
        print(f"\nScore: {score}/100")

        show_quality_results(post)

        print("\n1. Approve")
        print("2. Edit")
        print("3. Save as Draft")
        print("4. Cancel")

        choice = input("\nChoose an action: ").strip()

        if choice == "1":
            if not content_is_original(post):
                print("\nWARNING: This post appears similar to existing content.")
                continue

            save_approved_post(post, topic, post_type, score)
            print("\nPost approved and saved.")
            return

        elif choice == "2":
            edited_post = input("\nEnter your edited post:\n").strip()

            if not edited_post:
                print("Post cannot be empty.")
                continue

            post = edited_post
            score = calculate_score(post)
            print(f"\nNew score: {score}/100")

        elif choice == "3":
            save_draft(topic, post_type, post, score)
            return

        elif choice == "4":
            print("\nPost cancelled.")
            return

        else:
            print("Invalid choice.")


def generate_new_post():
    show_personality()
    show_brand_voice()

    topic = input("\nEnter a gaming topic: ").strip()

    if not topic:
        print("Topic cannot be empty.")
        return

    print("\nChoose a post type:")
    print("1. Gaming Question")
    print("2. Hot Take")
    print("3. News Reaction")
    print("4. Streaming Post")
    print("5. Meme Style")

    type_choice = input("\nChoose a post type: ").strip()

    post_types = {
        "1": "Gaming Question",
        "2": "Hot Take",
        "3": "News Reaction",
        "4": "Streaming Post",
        "5": "Meme Style",
    }

    post_type = post_types.get(type_choice)

    if not post_type:
        print("Invalid post type.")
        return

    print(f"\nPurpose: {POST_TYPE_PURPOSES[post_type]}")
    print(f"Brand voice: {BRAND_VOICE['Writing Style']}")

    posts = generate_posts(topic, post_type)

    if not posts:
        print("Unable to generate posts.")
        return

    print("\n--- GENERATED POSTS ---")

    scored_posts = []

    for index, post in enumerate(posts, start=1):
        score = calculate_score(post)
        scored_posts.append((post, score))

        print(f"\nOPTION {index}")
        print(post)
        print(f"Engagement score: {score}/100")

    best_post, best_score = max(scored_posts, key=lambda item: item[1])

    print("\n--- NEORUINS RECOMMENDATION ---")
    print("Based on the current rule-based scoring system:")
    print(best_post)
    print(f"Score: {best_score}/100")

    selection = input(
        "\nChoose an option to review (1-3), or press Enter to cancel: "
    ).strip()

    if selection not in ["1", "2", "3"]:
        print("\nGeneration cancelled.")
        return

    selected_post, selected_score = scored_posts[int(selection) - 1]

    review_post(selected_post, topic, post_type, selected_score)


def view_approved_posts():
    print("\n--- APPROVED POSTS ---")

    if not APPROVED_FILE.exists():
        print("No approved posts yet.")
        return

    content = APPROVED_FILE.read_text(encoding="utf-8").strip()

    if not content:
        print("No approved posts yet.")
        return

    print(content)


def view_content_history():
    print("\n--- CONTENT HISTORY ---")

    if not HISTORY_FILE.exists():
        print("No content history yet.")
        return

    content = HISTORY_FILE.read_text(encoding="utf-8").strip()

    if not content:
        print("No content history yet.")
        return

    print(content)


def view_drafts():
    drafts = load_drafts()

    print("\n--- DRAFTS ---")

    if not drafts:
        print("No drafts available.")
        return

    for index, draft in enumerate(drafts, start=1):
        print(f"\nDRAFT {index}")
        print(f"Topic: {draft['topic']}")
        print(f"Post Type: {draft['post_type']}")
        print(f"Score: {draft['score']}")
        print(f"Scheduled For: {draft['scheduled_for']}")
        print(f"Post: {draft['post']}")


def review_drafts():
    drafts = load_drafts()

    if not drafts:
        print("\nNo drafts available.")
        return

    while True:
        print("\n--- REVIEW DRAFTS ---")

        for index, draft in enumerate(drafts, start=1):
            print(
                f"{index}. {draft['topic']} | "
                f"{draft['post_type']} | "
                f"{draft['scheduled_for']}"
            )

        print("0. Return")

        choice = input("\nChoose a draft: ").strip()

        if choice == "0":
            return

        if not choice.isdigit() or not 1 <= int(choice) <= len(drafts):
            print("Invalid selection.")
            continue

        index = int(choice) - 1
        draft = drafts[index]

        print("\n--- DRAFT REVIEW ---")
        print(f"Topic: {draft['topic']}")
        print(f"Post Type: {draft['post_type']}")
        print(f"Scheduled For: {draft['scheduled_for']}")
        print(f"\n{draft['post']}")
        print(f"\nScore: {draft['score']}")

        show_quality_results(draft["post"])

        print("\n1. Approve")
        print("2. Edit")
        print("3. Delete")
        print("4. Return")

        action = input("\nChoose an action: ").strip()

        if action == "1":
            score = calculate_score(draft["post"])

            save_approved_post(
                draft["post"],
                draft["topic"],
                draft["post_type"],
                score,
            )

            drafts.pop(index)
            write_drafts(drafts)

            print("\nDraft approved and moved to approved posts.")

        elif action == "2":
            edited_post = input("\nEnter the edited post:\n").strip()

            if not edited_post:
                print("Post cannot be empty.")
                continue

            draft["post"] = edited_post
            draft["score"] = f"{calculate_score(edited_post)}/100"

            write_drafts(drafts)
            print("\nDraft updated.")

        elif action == "3":
            drafts.pop(index)
            write_drafts(drafts)
            print("\nDraft deleted.")

        elif action == "4":
            continue

        else:
            print("Invalid choice.")


def content_calendar():
    drafts = load_drafts()
    scheduled = []

    for draft in drafts:
        schedule = parse_schedule(draft["scheduled_for"])

        if schedule:
            scheduled.append((schedule, draft))

    print("\n--- CONTENT CALENDAR ---")

    if not scheduled:
        print("No scheduled posts.")
        return

    scheduled.sort(key=lambda item: item[0])
    current_date = None

    for schedule, draft in scheduled:
        date_text = schedule.strftime("%Y-%m-%d")

        if date_text != current_date:
            current_date = date_text
            print(f"\n=== {schedule.strftime('%A, %B %d, %Y')} ===")

        print(f"Time: {schedule.strftime('%I:%M %p')}")
        print(f"Topic: {draft['topic']}")
        print(f"Post Type: {draft['post_type']}")
        print(f"Score: {draft['score']}")
        print(f"Post: {draft['post']}")
        print("-" * 50)

    print(f"\nTotal scheduled posts: {len(scheduled)}")


def manage_drafts():
    drafts = load_drafts()

    if not drafts:
        print("\nNo drafts available.")
        return

    while True:
        print("\n--- MANAGE DRAFTS ---")

        for index, draft in enumerate(drafts, start=1):
            print(f"{index}. {draft['topic']} | {draft['scheduled_for']}")

        print("0. Return")

        choice = input("\nChoose a draft: ").strip()

        if choice == "0":
            return

        if not choice.isdigit() or not 1 <= int(choice) <= len(drafts):
            print("Invalid selection.")
            continue

        index = int(choice) - 1
        draft = drafts[index]

        print("\n--- DRAFT MANAGEMENT ---")
        print(f"Topic: {draft['topic']}")
        print(f"Post Type: {draft['post_type']}")
        print(f"Scheduled For: {draft['scheduled_for']}")

        print("\n1. Change Scheduled Date/Time")
        print("2. Unschedule")
        print("3. Delete")
        print("4. Return")

        action = input("\nChoose an action: ").strip()

        if action == "1":
            new_schedule = valid_future_schedule()

            if new_schedule == "Not scheduled":
                draft["scheduled_for"] = "Not scheduled"
                write_drafts(drafts)
                print("\nDraft unscheduled.")
                continue

            conflict = schedule_conflict(
                new_schedule,
                drafts,
                ignore_index=index,
            )

            if conflict:
                print("\nSCHEDULE CONFLICT DETECTED.")
                print(f"Existing topic: {conflict['topic']}")
                print(f"Existing post type: {conflict['post_type']}")
                print(f"Scheduled for: {conflict['scheduled_for']}")
                continue

            warning = frequency_warning(
                new_schedule,
                drafts,
                ignore_index=index,
            )

            show_frequency_warning(warning)
            show_posting_time_recommendations()

            draft["scheduled_for"] = new_schedule
            write_drafts(drafts)

            print("\nSchedule updated.")

        elif action == "2":
            draft["scheduled_for"] = "Not scheduled"
            write_drafts(drafts)
            print("\nDraft unscheduled.")

        elif action == "3":
            drafts.pop(index)
            write_drafts(drafts)
            print("\nDraft deleted.")

        elif action == "4":
            continue

        else:
            print("Invalid choice.")


def load_approved_post_records():
    records = []

    if not APPROVED_FILE.exists():
        return records

    content = APPROVED_FILE.read_text(encoding="utf-8").strip()

    if not content:
        return records

    # New structured format used by the current bot.
    if "--- APPROVED POST ---" in content:
        blocks = content.split("--- APPROVED POST ---")

        for block in blocks:
            if not block.strip():
                continue

            record = {
                "date": "",
                "topic": "",
                "post_type": "",
                "score": "",
                "post": "",
            }

            lines = block.splitlines()
            post_lines = []
            reading_post = False

            for line in lines:
                stripped_line = line.strip()

                if stripped_line.startswith("Date:"):
                    record["date"] = stripped_line.replace(
                        "Date:", "", 1
                    ).strip()
                    reading_post = False

                elif stripped_line.startswith("Topic:"):
                    record["topic"] = stripped_line.replace(
                        "Topic:", "", 1
                    ).strip()
                    reading_post = False

                elif stripped_line.startswith("Post Type:"):
                    record["post_type"] = stripped_line.replace(
                        "Post Type:", "", 1
                    ).strip()
                    reading_post = False

                elif stripped_line.startswith("Score:"):
                    record["score"] = stripped_line.replace(
                        "Score:", "", 1
                    ).strip()
                    reading_post = False

                elif stripped_line.startswith("Post:"):
                    record["post"] = stripped_line.replace(
                        "Post:", "", 1
                    ).strip()
                    reading_post = True

                elif reading_post:
                    post_lines.append(line)

            if post_lines:
                extra_post_text = "\n".join(post_lines).rstrip()

                if extra_post_text:
                    record["post"] = (
                        record["post"] + "\n" + extra_post_text
                    ).strip()

            if record["post"].strip():
                records.append(record)

    # Older approved_posts.txt format from earlier versions of NEORUINS.
    # These records may contain only the post text followed by an
    # "Engagement Score:" line and a dashed separator.
    else:
        legacy_blocks = re.split(r"\n-{10,}\n", content)

        for block in legacy_blocks:
            lines = [
                line.rstrip()
                for line in block.splitlines()
                if line.strip()
            ]

            if not lines:
                continue

            score = ""
            post_lines = []

            for line in lines:
                stripped_line = line.strip()

                if stripped_line.startswith("Engagement Score:"):
                    score = stripped_line.replace(
                        "Engagement Score:", "", 1
                    ).strip()
                else:
                    post_lines.append(line)

            post = "\n".join(post_lines).strip()

            if not post:
                continue

            records.append({
                "date": "Legacy post",
                "topic": "Legacy approved post",
                "post_type": "Legacy",
                "score": score,
                "post": post,
            })

    return records

def get_positive_number(prompt):
    while True:
        value = input(prompt).strip()

        if value.upper() == "CANCEL":
            return None

        try:
            number = float(value)

            if number < 0:
                print("Please enter a number of 0 or greater.")
                continue

            return number

        except ValueError:
            print("Please enter a valid number, or type CANCEL to stop tracking.")


def calculate_performance_score(likes, reposts, replies, bookmarks, views):
    engagement_actions = (
        likes
        + (reposts * 2)
        + (replies * 2)
        + (bookmarks * 2)
    )

    if views <= 0:
        return 0

    engagement_rate = (engagement_actions / views) * 100
    score = engagement_rate * 10

    return round(min(score, 100), 2)


def get_posted_at():
    while True:
        posted_at = input(
            "\nPosted At (YYYY-MM-DD HH:MM, or press Enter if not posted yet): "
        ).strip()

        if not posted_at:
            return ""

        if posted_at.upper() == "CANCEL":
            return None

        try:
            parsed = datetime.strptime(posted_at, "%Y-%m-%d %H:%M")
            return parsed.strftime("%Y-%m-%d %H:%M")
        except ValueError:
            print(
                "Invalid date/time. Please use YYYY-MM-DD HH:MM, "
                "or type CANCEL to stop tracking."
            )


def fetch_x_post_metrics(post_id):
    load_dotenv()

    api_key = os.getenv("X_API_KEY")
    api_key_secret = os.getenv("X_API_KEY_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

    if not all([
        api_key,
        api_key_secret,
        access_token,
        access_token_secret,
    ]):
        print("\nERROR: One or more X credentials are missing.")
        return None

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_key_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    try:
        response = client.get_tweet(
            post_id,
            tweet_fields=[
                "created_at",
                "public_metrics",
                "non_public_metrics",
                "organic_metrics",
            ],
            user_auth=True,
        )

        if response.data is None:
            print("\nERROR: X did not return post data.")
            return None

        public_metrics = response.data.public_metrics or {}
        non_public_metrics = response.data.non_public_metrics or {}
        organic_metrics = response.data.organic_metrics or {}

        created_at = response.data.created_at
        posted_at = ""

        if created_at:
            # X returns an offset-aware UTC timestamp. Convert it to the
            # computer's local timezone so the existing posting-time analytics
            # continue to use local publication time.
            local_created_at = created_at.astimezone()
            posted_at = local_created_at.strftime("%Y-%m-%d %H:%M")

        return {
            "post_id": str(response.data.id),
            "posted_at": posted_at,
            "likes": float(public_metrics.get("like_count", 0)),
            "reposts": float(public_metrics.get("retweet_count", 0)),
            "replies": float(public_metrics.get("reply_count", 0)),
            "bookmarks": float(public_metrics.get("bookmark_count", 0)),
            "views": float(public_metrics.get("impression_count", 0)),
            "quotes": float(public_metrics.get("quote_count", 0)),
            "engagements": float(non_public_metrics.get("engagements", 0)),
            "profile_clicks": float(
                non_public_metrics.get(
                    "user_profile_clicks",
                    organic_metrics.get("user_profile_clicks", 0),
                )
            ),
        }

    except tweepy.TweepyException as error:
        print("\nX API ERROR:")
        print(error)
        return None


def save_performance_record(
    selected_post,
    x_post_id,
    posted_at,
    likes,
    reposts,
    replies,
    bookmarks,
    views,
    score,
    data_source="Manual Entry",
    quotes=None,
    engagements=None,
    profile_clicks=None,
):
    with open(PERFORMANCE_FILE, "a", encoding="utf-8") as file:
        file.write("\n--- PERFORMANCE RECORD ---\n")
        file.write(
            f"Date Tracked: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file.write(f"Data Source: {data_source}\n")
        file.write(f"X Post ID: {x_post_id}\n")
        file.write(f"Posted At: {posted_at}\n")
        file.write(f"Post Type: {selected_post['post_type']}\n")
        file.write(f"Post: {selected_post['post']}\n")
        file.write(f"Likes: {likes}\n")
        file.write(f"Reposts: {reposts}\n")
        file.write(f"Replies: {replies}\n")
        file.write(f"Bookmarks: {bookmarks}\n")
        file.write(f"Views: {views}\n")

        if quotes is not None:
            file.write(f"Quote Posts: {quotes}\n")
        if engagements is not None:
            file.write(f"X Engagements: {engagements}\n")
        if profile_clicks is not None:
            file.write(f"Profile Clicks: {profile_clicks}\n")

        file.write(f"Performance Score: {score}\n")


def track_post_performance():
    posts = load_approved_post_records()

    if not posts:
        print("\nNo approved posts available to track.")
        return

    print("\n--- TRACK POST PERFORMANCE ---")

    for index, record in enumerate(posts, start=1):
        published = find_published_record(record["post"])
        post_id = published["post_id"] if published else ""
        x_status = f"X ID {post_id}" if post_id else "No X ID recorded"

        print(
            f"{index}. {record['topic']} | "
            f"{record['post_type']} | "
            f"{record['date']} | "
            f"{x_status}"
        )

    choice = input(
        "\nChoose the post you want to track (or 0 to cancel): "
    ).strip()

    if choice == "0":
        return

    if not choice.isdigit() or not 1 <= int(choice) <= len(posts):
        print("Invalid selection.")
        return

    selected_post = posts[int(choice) - 1]
    published = find_published_record(selected_post["post"])

    print("\n--- SELECTED POST ---")
    print(selected_post["post"])

    x_post_id = ""
    posted_at = ""

    if published:
        x_post_id = published["post_id"]
        posted_at = published_time_for_performance(published["published_at"])

        print("\n--- X PUBLICATION RECORD ---")
        print(f"X Post ID: {x_post_id or 'Not recorded'}")
        print(f"Account: {published['account'] or 'Not recorded'}")
        print(f"Published At: {published['published_at'] or 'Not recorded'}")
    else:
        print("\nNo matching X publication record was found for this post.")

    if x_post_id:
        print("\n1. Retrieve Live Metrics from X")
        print("2. Enter Metrics Manually")
        print("0. Cancel")

        tracking_choice = input("\nChoose a tracking method: ").strip()

        if tracking_choice == "0":
            print("\nPerformance tracking cancelled. No record was saved.")
            return

        if tracking_choice == "1":
            print("\nRetrieving live performance data from X...")
            metrics = fetch_x_post_metrics(x_post_id)

            if metrics is None:
                print("\nLive X metrics were not saved.")
                print("You can run Option 8 again and choose manual entry if needed.")
                return

            # Prefer X's authoritative creation time when available. This also
            # fills the timestamp for older migrated publication records.
            if metrics["posted_at"]:
                posted_at = metrics["posted_at"]

            likes = metrics["likes"]
            reposts = metrics["reposts"]
            replies = metrics["replies"]
            bookmarks = metrics["bookmarks"]
            views = metrics["views"]

            score = calculate_performance_score(
                likes,
                reposts,
                replies,
                bookmarks,
                views,
            )

            print("\n--- LIVE X METRICS ---")
            print(f"Posted At: {posted_at or 'Not available'}")
            print(f"Likes: {likes:g}")
            print(f"Reposts: {reposts:g}")
            print(f"Replies: {replies:g}")
            print(f"Bookmarks: {bookmarks:g}")
            print(f"Views: {views:g}")
            print(f"Quote Posts: {metrics['quotes']:g}")
            print(f"X Engagements: {metrics['engagements']:g}")
            print(f"Profile Clicks: {metrics['profile_clicks']:g}")
            print(f"Performance Score: {score}/100")

            print("\nSave these live X metrics to performance_history.txt?")
            confirmation = input("Type YES to save, or anything else to cancel: ").strip()

            if confirmation != "YES":
                print("\nPerformance tracking cancelled. No record was saved.")
                return

            save_performance_record(
                selected_post=selected_post,
                x_post_id=x_post_id,
                posted_at=posted_at,
                likes=likes,
                reposts=reposts,
                replies=replies,
                bookmarks=bookmarks,
                views=views,
                score=score,
                data_source="X API",
                quotes=metrics["quotes"],
                engagements=metrics["engagements"],
                profile_clicks=metrics["profile_clicks"],
            )

            print("\nPerformance recorded successfully from X.")
            print(f"X Post ID: {x_post_id}")
            print(f"Performance Score: {score}/100")
            return

        if tracking_choice != "2":
            print("\nInvalid selection. No record was saved.")
            return

    if not posted_at:
        if published:
            print(
                "\nA valid publication time is not available for this record."
            )
        posted_at = get_posted_at()

        if posted_at is None:
            print("\nPerformance tracking cancelled. No record was saved.")
            return
    elif published:
        print("\nPosting time loaded automatically from published_posts.txt.")

    print("\nEnter the performance numbers from X.")
    print("Type CANCEL at any performance prompt to stop without saving.")

    likes = get_positive_number("Likes: ")
    if likes is None:
        print("\nPerformance tracking cancelled. No record was saved.")
        return

    reposts = get_positive_number("Reposts: ")
    if reposts is None:
        print("\nPerformance tracking cancelled. No record was saved.")
        return

    replies = get_positive_number("Replies: ")
    if replies is None:
        print("\nPerformance tracking cancelled. No record was saved.")
        return

    bookmarks = get_positive_number("Bookmarks: ")
    if bookmarks is None:
        print("\nPerformance tracking cancelled. No record was saved.")
        return

    views = get_positive_number("Views: ")
    if views is None:
        print("\nPerformance tracking cancelled. No record was saved.")
        return

    score = calculate_performance_score(
        likes,
        reposts,
        replies,
        bookmarks,
        views,
    )

    save_performance_record(
        selected_post=selected_post,
        x_post_id=x_post_id,
        posted_at=posted_at,
        likes=likes,
        reposts=reposts,
        replies=replies,
        bookmarks=bookmarks,
        views=views,
        score=score,
        data_source="Manual Entry",
    )

    print("\nPerformance recorded successfully.")

    if x_post_id:
        print(f"X Post ID: {x_post_id}")

    print(f"Performance Score: {score}/100")

def view_performance_history():
    print("\n--- PERFORMANCE HISTORY ---")

    if not PERFORMANCE_FILE.exists():
        print("No performance data yet.")
        return

    content = PERFORMANCE_FILE.read_text(encoding="utf-8").strip()

    if not content:
        print("No performance data yet.")
        return

    print(content)


def load_performance_records():
    records = []

    if not PERFORMANCE_FILE.exists():
        return records

    content = PERFORMANCE_FILE.read_text(encoding="utf-8").strip()

    if not content:
        return records

    blocks = content.split("\n--- PERFORMANCE RECORD ---\n")

    for block in blocks:
        if not block.strip():
            continue

        record = {
            "date_tracked": "",
            "data_source": "",
            "x_post_id": "",
            "posted_at": "",
            "post_type": "",
            "post": "",
            "likes": 0,
            "reposts": 0,
            "replies": 0,
            "bookmarks": 0,
            "views": 0,
            "performance_score": 0,
        }

        for line in block.splitlines():
            if line.startswith("Date Tracked:"):
                record["date_tracked"] = line.replace(
                    "Date Tracked:", "", 1
                ).strip()

            elif line.startswith("Data Source:"):
                record["data_source"] = line.replace(
                    "Data Source:", "", 1
                ).strip()

            elif line.startswith("X Post ID:"):
                record["x_post_id"] = line.replace(
                    "X Post ID:", "", 1
                ).strip()

            elif line.startswith("Posted At:"):
                record["posted_at"] = line.replace(
                    "Posted At:", "", 1
                ).strip()

            elif line.startswith("Post Type:"):
                record["post_type"] = line.replace(
                    "Post Type:", "", 1
                ).strip()

            elif line.startswith("Post:"):
                record["post"] = line.replace(
                    "Post:", "", 1
                ).strip()

            elif line.startswith("Likes:"):
                record["likes"] = float(
                    line.replace("Likes:", "", 1).strip()
                )

            elif line.startswith("Reposts:"):
                record["reposts"] = float(
                    line.replace("Reposts:", "", 1).strip()
                )

            elif line.startswith("Replies:"):
                record["replies"] = float(
                    line.replace("Replies:", "", 1).strip()
                )

            elif line.startswith("Bookmarks:"):
                record["bookmarks"] = float(
                    line.replace("Bookmarks:", "", 1).strip()
                )

            elif line.startswith("Views:"):
                record["views"] = float(
                    line.replace("Views:", "", 1).strip()
                )

            elif line.startswith("Performance Score:"):
                score_text = line.replace(
                    "Performance Score:", "", 1
                ).strip()

                if "/" in score_text:
                    score_text = score_text.split("/", 1)[0].strip()

                try:
                    record["performance_score"] = float(score_text)
                except ValueError:
                    record["performance_score"] = 0

        records.append(record)

    return records


def performance_analytics():
    records = load_performance_records()

    print("\n--- PERFORMANCE ANALYTICS ---")

    if not records:
        print("No performance data available yet.")
        return

    total_posts = len(records)

    avg_views = sum(r["views"] for r in records) / total_posts
    avg_likes = sum(r["likes"] for r in records) / total_posts
    avg_reposts = sum(r["reposts"] for r in records) / total_posts
    avg_replies = sum(r["replies"] for r in records) / total_posts
    avg_bookmarks = sum(r["bookmarks"] for r in records) / total_posts
    avg_score = sum(r["performance_score"] for r in records) / total_posts

    best_record = max(
        records,
        key=lambda r: r["performance_score"],
    )

    print(f"Posts tracked: {total_posts}")
    print(f"Average views: {avg_views:.2f}")
    print(f"Average likes: {avg_likes:.2f}")
    print(f"Average reposts: {avg_reposts:.2f}")
    print(f"Average replies: {avg_replies:.2f}")
    print(f"Average bookmarks: {avg_bookmarks:.2f}")
    print(f"Average performance score: {avg_score:.2f}/100")

    print("\n--- HIGHEST PERFORMANCE SCORE ---")
    print(f"Score: {best_record['performance_score']}/100")
    print(f"Post Type: {best_record['post_type']}")
    print(f"Post: {best_record['post']}")


def post_type_analytics():
    records = load_performance_records()

    print("\n--- POST TYPE ANALYTICS ---")

    if not records:
        print("No performance data available yet.")
        return

    post_types = [
        "Gaming Question",
        "Hot Take",
        "News Reaction",
        "Streaming Post",
        "Meme Style",
    ]

    for post_type in post_types:
        matching = [
            record
            for record in records
            if record["post_type"] == post_type
        ]

        print(f"\n--- {post_type} ---")

        if not matching:
            print("No tracked posts for this type yet.")
            continue

        count = len(matching)

        avg_views = sum(r["views"] for r in matching) / count
        avg_likes = sum(r["likes"] for r in matching) / count
        avg_reposts = sum(r["reposts"] for r in matching) / count
        avg_replies = sum(r["replies"] for r in matching) / count
        avg_bookmarks = sum(r["bookmarks"] for r in matching) / count
        avg_score = (
            sum(r["performance_score"] for r in matching) / count
        )

        print(f"Posts tracked: {count}")
        print(f"Average views: {avg_views:.2f}")
        print(f"Average likes: {avg_likes:.2f}")
        print(f"Average reposts: {avg_reposts:.2f}")
        print(f"Average replies: {avg_replies:.2f}")
        print(f"Average bookmarks: {avg_bookmarks:.2f}")
        print(f"Average performance score: {avg_score:.2f}/100")


def posting_time_analytics():
    records = load_performance_records()

    print("\n--- POSTING TIME ANALYTICS ---")

    if not records:
        print("No performance data available yet.")
        return

    timed_records = []

    for record in records:
        if not record.get("posted_at"):
            continue

        try:
            posted_date = datetime.strptime(
                record["posted_at"],
                "%Y-%m-%d %H:%M",
            )
            timed_records.append((posted_date, record))
        except ValueError:
            continue

    if not timed_records:
        print("No actual publication-time data available yet.")
        print(
            "When tracking a new post, enter the date/time when it was "
            "actually published."
        )
        return

    time_periods = {
        "Morning (5 AM - 11 AM)": [],
        "Midday (11 AM - 2 PM)": [],
        "Afternoon (2 PM - 5 PM)": [],
        "Evening (5 PM - 9 PM)": [],
        "Night (9 PM - 5 AM)": [],
    }

    for posted_date, record in timed_records:
        hour = posted_date.hour

        if 5 <= hour < 11:
            time_periods["Morning (5 AM - 11 AM)"].append(record)
        elif 11 <= hour < 14:
            time_periods["Midday (11 AM - 2 PM)"].append(record)
        elif 14 <= hour < 17:
            time_periods["Afternoon (2 PM - 5 PM)"].append(record)
        elif 17 <= hour < 21:
            time_periods["Evening (5 PM - 9 PM)"].append(record)
        else:
            time_periods["Night (9 PM - 5 AM)"].append(record)

    print(
        "\nThis analysis uses the actual publication time entered "
        "for each tracked post."
    )

    for period, matching in time_periods.items():
        print(f"\n--- {period} ---")

        if not matching:
            print("No tracked posts in this period yet.")
            continue

        count = len(matching)
        avg_views = sum(r["views"] for r in matching) / count
        avg_score = sum(r["performance_score"] for r in matching) / count
        avg_likes = sum(r["likes"] for r in matching) / count
        avg_reposts = sum(r["reposts"] for r in matching) / count
        avg_replies = sum(r["replies"] for r in matching) / count

        print(f"Posts tracked: {count}")
        print(f"Average views: {avg_views:.2f}")
        print(f"Average likes: {avg_likes:.2f}")
        print(f"Average reposts: {avg_reposts:.2f}")
        print(f"Average replies: {avg_replies:.2f}")
        print(f"Average performance score: {avg_score:.2f}/100")

    print("\n--- IMPORTANT ---")
    print(
        "A larger sample is needed before treating differences between "
        "time periods as meaningful patterns."
    )


def posting_hour_analytics():
    records = load_performance_records()

    print("\n--- POSTING HOUR ANALYTICS ---")

    if not records:
        print("No performance data available yet.")
        return

    hour_records = {hour: [] for hour in range(24)}

    for record in records:
        if not record.get("posted_at"):
            continue

        try:
            posted_date = datetime.strptime(
                record["posted_at"],
                "%Y-%m-%d %H:%M",
            )
            hour_records[posted_date.hour].append(record)
        except ValueError:
            continue

    if not any(hour_records.values()):
        print("No actual publication-time data available yet.")
        print(
            "When tracking a new post, enter the date/time when it was "
            "actually published."
        )
        return

    print("\nThis analysis groups tracked posts by the exact hour they were published.")

    for hour in range(24):
        matching = hour_records[hour]

        if not matching:
            continue

        count = len(matching)
        avg_views = sum(r["views"] for r in matching) / count
        avg_score = sum(r["performance_score"] for r in matching) / count
        avg_likes = sum(r["likes"] for r in matching) / count
        avg_reposts = sum(r["reposts"] for r in matching) / count
        avg_replies = sum(r["replies"] for r in matching) / count

        display_hour = datetime.strptime(str(hour), "%H").strftime("%I %p").lstrip("0")

        print(f"\n--- {display_hour} ---")
        print(f"Posts tracked: {count}")
        print(f"Average views: {avg_views:.2f}")
        print(f"Average likes: {avg_likes:.2f}")
        print(f"Average reposts: {avg_reposts:.2f}")
        print(f"Average replies: {avg_replies:.2f}")
        print(f"Average performance score: {avg_score:.2f}/100")

    print("\n--- IMPORTANT ---")
    print(
        "Use several posts at each hour before treating differences as "
        "meaningful patterns. This is a measurement tool, not a guarantee "
        "of future performance."
    )


def posting_hour_insights():
    records = load_performance_records()

    print("\n--- POSTING HOUR INSIGHTS ---")

    if not records:
        print("No performance data available yet.")
        return

    hour_records = {hour: [] for hour in range(24)}

    for record in records:
        if not record.get("posted_at"):
            continue

        try:
            posted_date = datetime.strptime(
                record["posted_at"],
                "%Y-%m-%d %H:%M",
            )
            hour_records[posted_date.hour].append(record)
        except ValueError:
            continue

    usable_hours = []

    for hour, matching in hour_records.items():
        if len(matching) < 3:
            continue

        avg_score = sum(r["performance_score"] for r in matching) / len(matching)
        avg_views = sum(r["views"] for r in matching) / len(matching)

        usable_hours.append({
            "hour": hour,
            "count": len(matching),
            "avg_score": avg_score,
            "avg_views": avg_views,
        })

    if not usable_hours:
        print(
            "Not enough data yet. Track at least 3 posts at the same "
            "publication hour to generate an hour insight."
        )
        return

    usable_hours.sort(key=lambda item: item["avg_score"], reverse=True)

    print(
        "\nHours shown here have at least 3 tracked posts. "
        "They are ordered by average performance score."
    )

    for position, item in enumerate(usable_hours, start=1):
        display_hour = datetime.strptime(
            str(item["hour"]),
            "%H",
        ).strftime("%I %p").lstrip("0")

        print(f"\n{position}. {display_hour}")
        print(f"Posts tracked: {item['count']}")
        print(f"Average performance score: {item['avg_score']:.2f}/100")
        print(f"Average views: {item['avg_views']:.2f}")

    top = usable_hours[0]
    top_display_hour = datetime.strptime(
        str(top["hour"]),
        "%H",
    ).strftime("%I %p").lstrip("0")

    print("\n--- DATA-BASED TESTING SUGGESTION ---")
    print(
        f"Among hours with at least 3 tracked posts, {top_display_hour} "
        f"currently has the highest average performance score "
        f"({top['avg_score']:.2f}/100)."
    )
    print(
        "Treat this as a testing signal, not a guarantee. Continue tracking "
        "posts before changing your posting schedule."
    )


def posting_day_analytics():
    records = load_performance_records()

    print("\n--- POSTING DAY ANALYTICS ---")

    if not records:
        print("No performance data available yet.")
        return

    day_records = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }

    for record in records:
        if not record.get("posted_at"):
            continue

        try:
            posted_date = datetime.strptime(
                record["posted_at"],
                "%Y-%m-%d %H:%M",
            )
            day_records[posted_date.strftime("%A")].append(record)
        except ValueError:
            continue

    if not any(day_records.values()):
        print("No actual publication-time data available yet.")
        print(
            "When tracking a new post, enter the date/time when it was "
            "actually published."
        )
        return

    print("\nThis analysis groups tracked posts by the day they were published.")

    for day, matching in day_records.items():
        if not matching:
            continue

        count = len(matching)
        avg_views = sum(r["views"] for r in matching) / count
        avg_likes = sum(r["likes"] for r in matching) / count
        avg_reposts = sum(r["reposts"] for r in matching) / count
        avg_replies = sum(r["replies"] for r in matching) / count
        avg_score = sum(r["performance_score"] for r in matching) / count

        print(f"\n--- {day} ---")
        print(f"Posts tracked: {count}")
        print(f"Average views: {avg_views:.2f}")
        print(f"Average likes: {avg_likes:.2f}")
        print(f"Average reposts: {avg_reposts:.2f}")
        print(f"Average replies: {avg_replies:.2f}")
        print(f"Average performance score: {avg_score:.2f}/100")

    print("\n--- IMPORTANT ---")
    print(
        "Use several posts on each day before treating differences as "
        "meaningful patterns. This is a measurement tool, not a guarantee "
        "of future performance."
    )


def posting_day_insights():
    records = load_performance_records()

    print("\n--- POSTING DAY INSIGHTS ---")

    if not records:
        print("No performance data available yet.")
        return

    day_records = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }

    for record in records:
        if not record.get("posted_at"):
            continue

        try:
            posted_date = datetime.strptime(
                record["posted_at"],
                "%Y-%m-%d %H:%M",
            )
            day_records[posted_date.strftime("%A")].append(record)
        except ValueError:
            continue

    usable_days = []

    for day, matching in day_records.items():
        if len(matching) < 3:
            continue

        avg_score = sum(
            r["performance_score"] for r in matching
        ) / len(matching)

        avg_views = sum(
            r["views"] for r in matching
        ) / len(matching)

        usable_days.append({
            "day": day,
            "count": len(matching),
            "avg_score": avg_score,
            "avg_views": avg_views,
        })

    if not usable_days:
        print(
            "Not enough data yet. Track at least 3 posts on the "
            "same day of the week to generate a day insight."
        )
        return

    usable_days.sort(
        key=lambda item: item["avg_score"],
        reverse=True,
    )

    print(
        "\nDays shown here have at least 3 tracked posts. "
        "They are ordered by average performance score."
    )

    for position, item in enumerate(usable_days, start=1):
        print(f"\n{position}. {item['day']}")
        print(f"Posts tracked: {item['count']}")
        print(
            f"Average performance score: "
            f"{item['avg_score']:.2f}/100"
        )
        print(f"Average views: {item['avg_views']:.2f}")

    top = usable_days[0]

    print("\n--- DATA-BASED TESTING SUGGESTION ---")
    print(
        f"Among days with at least 3 tracked posts, "
        f"{top['day']} currently has the highest average "
        f"performance score ({top['avg_score']:.2f}/100)."
    )
    print(
        "Treat this as a testing signal, not a guarantee. "
        "Continue tracking posts before changing your posting schedule."
    )


def posting_schedule_insights():
    records = load_performance_records()

    print("\n--- POSTING SCHEDULE INSIGHTS ---")

    if not records:
        print("No performance data available yet.")
        return

    schedule_records = {}

    for record in records:
        if not record.get("posted_at"):
            continue

        try:
            posted_date = datetime.strptime(
                record["posted_at"],
                "%Y-%m-%d %H:%M",
            )
        except ValueError:
            continue

        day = posted_date.strftime("%A")
        hour = posted_date.hour
        key = (day, hour)

        if key not in schedule_records:
            schedule_records[key] = []

        schedule_records[key].append(record)

    usable_schedules = []

    for (day, hour), matching in schedule_records.items():
        if len(matching) < 3:
            continue

        avg_score = (
            sum(r["performance_score"] for r in matching)
            / len(matching)
        )

        avg_views = (
            sum(r["views"] for r in matching)
            / len(matching)
        )

        usable_schedules.append({
            "day": day,
            "hour": hour,
            "count": len(matching),
            "avg_score": avg_score,
            "avg_views": avg_views,
        })

    if not usable_schedules:
        print(
            "Not enough data yet. Track at least 3 posts at the "
            "same day and publication hour to generate a schedule insight."
        )
        return

    usable_schedules.sort(
        key=lambda item: item["avg_score"],
        reverse=True,
    )

    print(
        "\nDay/hour combinations shown here have at least 3 tracked posts. "
        "They are ordered by average performance score."
    )

    for position, item in enumerate(usable_schedules, start=1):
        display_hour = datetime.strptime(
            str(item["hour"]),
            "%H",
        ).strftime("%I %p").lstrip("0")

        print(f"\n{position}. {item['day']} at {display_hour}")
        print(f"Posts tracked: {item['count']}")
        print(
            f"Average performance score: "
            f"{item['avg_score']:.2f}/100"
        )
        print(f"Average views: {item['avg_views']:.2f}")

    top = usable_schedules[0]
    top_display_hour = datetime.strptime(
        str(top["hour"]),
        "%H",
    ).strftime("%I %p").lstrip("0")

    print("\n--- DATA-BASED TESTING SUGGESTION ---")
    print(
        f"Among day/hour combinations with at least 3 tracked posts, "
        f"{top['day']} at {top_display_hour} currently has the highest "
        f"average performance score ({top['avg_score']:.2f}/100)."
    )
    print(
        "Treat this as a testing signal, not a guarantee. Continue tracking "
        "more posts before changing your posting schedule."
    )


def content_strategy_insights():
    records = load_performance_records()

    print("\n--- CONTENT STRATEGY INSIGHTS ---")

    if not records:
        print("No performance data available yet.")
        return

    post_types = [
        "Gaming Question",
        "Hot Take",
        "News Reaction",
        "Streaming Post",
        "Meme Style",
    ]

    type_records = {post_type: [] for post_type in post_types}

    for record in records:
        post_type = record.get("post_type", "")

        if post_type in type_records:
            type_records[post_type].append(record)

    usable_types = []

    for post_type, matching in type_records.items():
        if len(matching) < 3:
            continue

        avg_score = sum(
            r["performance_score"] for r in matching
        ) / len(matching)

        avg_views = sum(
            r["views"] for r in matching
        ) / len(matching)

        usable_types.append({
            "post_type": post_type,
            "count": len(matching),
            "avg_score": avg_score,
            "avg_views": avg_views,
        })

    timed_records = []

    for record in records:
        if not record.get("posted_at"):
            continue

        try:
            posted_date = datetime.strptime(
                record["posted_at"],
                "%Y-%m-%d %H:%M",
            )
            timed_records.append((posted_date, record))
        except ValueError:
            continue

    day_hour_records = {}

    for posted_date, record in timed_records:
        key = (
            posted_date.strftime("%A"),
            posted_date.hour,
        )

        if key not in day_hour_records:
            day_hour_records[key] = []

        day_hour_records[key].append(record)

    usable_schedules = []

    for (day, hour), matching in day_hour_records.items():
        if len(matching) < 3:
            continue

        avg_score = sum(
            r["performance_score"] for r in matching
        ) / len(matching)

        avg_views = sum(
            r["views"] for r in matching
        ) / len(matching)

        usable_schedules.append({
            "day": day,
            "hour": hour,
            "count": len(matching),
            "avg_score": avg_score,
            "avg_views": avg_views,
        })

    print("\nThis analysis looks for patterns in your tracked content data.")
    print(
        "A category needs at least 3 tracked posts before it is included "
        "in the strategy summary."
    )

    print("\n--- CONTENT TYPE DATA ---")

    if not usable_types:
        print("No post type has enough data yet.")
    else:
        usable_types.sort(
            key=lambda item: item["avg_score"],
            reverse=True,
        )

        for item in usable_types:
            print(f"\n{item['post_type']}")
            print(f"Posts tracked: {item['count']}")
            print(
                f"Average performance score: "
                f"{item['avg_score']:.2f}/100"
            )
            print(f"Average views: {item['avg_views']:.2f}")

    print("\n--- DAY/HOUR DATA ---")

    if not usable_schedules:
        print("No day/hour combination has enough data yet.")
    else:
        usable_schedules.sort(
            key=lambda item: item["avg_score"],
            reverse=True,
        )

        for item in usable_schedules:
            display_hour = datetime.strptime(
                str(item["hour"]),
                "%H",
            ).strftime("%I %p").lstrip("0")

            print(
                f"\n{item['day']} at {display_hour}"
            )
            print(f"Posts tracked: {item['count']}")
            print(
                f"Average performance score: "
                f"{item['avg_score']:.2f}/100"
            )
            print(f"Average views: {item['avg_views']:.2f}")

    if not usable_types and not usable_schedules:
        print("\n--- NEXT DATA GOAL ---")
        print(
            "Track at least 3 posts of the same post type and at least "
            "3 posts at the same day/hour combination."
        )
        return

    print("\n--- STRATEGY TESTING SIGNAL ---")

    if usable_types and usable_schedules:
        top_type = usable_types[0]
        top_schedule = usable_schedules[0]

        top_display_hour = datetime.strptime(
            str(top_schedule["hour"]),
            "%H",
        ).strftime("%I %p").lstrip("0")

        print(
            f"Your current tracked data has a measurable signal for "
            f"{top_type['post_type']} content and "
            f"{top_schedule['day']} at {top_display_hour}."
        )
        print(
            f"{top_type['post_type']} average score: "
            f"{top_type['avg_score']:.2f}/100 "
            f"({top_type['count']} posts)"
        )
        print(
            f"{top_schedule['day']} at {top_display_hour} average score: "
            f"{top_schedule['avg_score']:.2f}/100 "
            f"({top_schedule['count']} posts)"
        )
        print(
            "\nUse this combination as a test to gather more comparable "
            "data. This is a testing signal, not a guarantee."
        )

    elif usable_types:
        top_type = usable_types[0]

        print(
            f"{top_type['post_type']} currently has the highest average "
            f"performance score among post types with at least 3 tracked "
            f"posts: {top_type['avg_score']:.2f}/100."
        )
        print(
            "Test this content type again while continuing to collect "
            "day/hour data. This is a testing signal, not a guarantee."
        )

    else:
        top_schedule = usable_schedules[0]

        top_display_hour = datetime.strptime(
            str(top_schedule["hour"]),
            "%H",
        ).strftime("%I %p").lstrip("0")

        print(
            f"{top_schedule['day']} at {top_display_hour} currently has "
            f"the highest average performance score among day/hour "
            f"combinations with at least 3 tracked posts: "
            f"{top_schedule['avg_score']:.2f}/100."
        )
        print(
            "Test this schedule again while continuing to collect "
            "content-type data. This is a testing signal, not a guarantee."
        )

    print("\n--- IMPORTANT ---")
    print(
        "These patterns describe your tracked data. They do not establish "
        "that content type, day, or time caused a performance difference."
    )



def content_schedule_insights():
    records = load_performance_records()

    print("\n--- CONTENT TYPE + SCHEDULE INSIGHTS ---")

    if not records:
        print("No performance data available yet.")
        return

    combination_records = {}

    for record in records:
        post_type = record.get("post_type", "")
        posted_at = record.get("posted_at", "")

        if not post_type or not posted_at:
            continue

        try:
            posted_date = datetime.strptime(
                posted_at,
                "%Y-%m-%d %H:%M",
            )
        except ValueError:
            continue

        day = posted_date.strftime("%A")
        hour = posted_date.hour
        key = (post_type, day, hour)

        if key not in combination_records:
            combination_records[key] = []

        combination_records[key].append(record)

    usable_combinations = []

    for (post_type, day, hour), matching in combination_records.items():
        if len(matching) < 3:
            continue

        avg_score = (
            sum(r["performance_score"] for r in matching)
            / len(matching)
        )

        avg_views = (
            sum(r["views"] for r in matching)
            / len(matching)
        )

        avg_likes = (
            sum(r["likes"] for r in matching)
            / len(matching)
        )

        avg_reposts = (
            sum(r["reposts"] for r in matching)
            / len(matching)
        )

        avg_replies = (
            sum(r["replies"] for r in matching)
            / len(matching)
        )

        avg_bookmarks = (
            sum(r["bookmarks"] for r in matching)
            / len(matching)
        )

        usable_combinations.append({
            "post_type": post_type,
            "day": day,
            "hour": hour,
            "count": len(matching),
            "avg_score": avg_score,
            "avg_views": avg_views,
            "avg_likes": avg_likes,
            "avg_reposts": avg_reposts,
            "avg_replies": avg_replies,
            "avg_bookmarks": avg_bookmarks,
        })

    if not usable_combinations:
        print(
            "Not enough data yet. Track at least 3 posts with the same "
            "content type, day, and publication hour to generate a "
            "combined insight."
        )
        return

    usable_combinations.sort(
        key=lambda item: item["avg_score"],
        reverse=True,
    )

    print(
        "\nCombinations shown here have at least 3 tracked posts with the "
        "same content type, day, and publication hour."
    )
    print("They are ordered by average performance score.")

    for position, item in enumerate(usable_combinations, start=1):
        display_hour = datetime.strptime(
            str(item["hour"]),
            "%H",
        ).strftime("%I %p").lstrip("0")

        print(
            f"\n{position}. {item['post_type']} | "
            f"{item['day']} at {display_hour}"
        )
        print(f"Posts tracked: {item['count']}")
        print(
            f"Average performance score: "
            f"{item['avg_score']:.2f}/100"
        )
        print(f"Average views: {item['avg_views']:.2f}")
        print(f"Average likes: {item['avg_likes']:.2f}")
        print(f"Average reposts: {item['avg_reposts']:.2f}")
        print(f"Average replies: {item['avg_replies']:.2f}")
        print(f"Average bookmarks: {item['avg_bookmarks']:.2f}")

    top = usable_combinations[0]
    top_display_hour = datetime.strptime(
        str(top["hour"]),
        "%H",
    ).strftime("%I %p").lstrip("0")

    print("\n--- DATA-BASED TESTING SUGGESTION ---")
    print(
        f"Among combinations with at least 3 tracked posts, "
        f"{top['post_type']} posted on {top['day']} at "
        f"{top_display_hour} currently has the highest average "
        f"performance score ({top['avg_score']:.2f}/100)."
    )
    print(
        "Use this combination as a testing signal and collect more "
        "comparable posts before making schedule or content changes. "
        "This is not a guarantee of future performance."
    )

    print("\n--- IMPORTANT ---")
    print(
        "These patterns describe your tracked data. They do not establish "
        "that content type, day, or time caused a performance difference."
    )

def performance_insights():
    all_records = load_performance_records()

    print("\n--- NEORUINS PERFORMANCE INSIGHTS ---")

    if not all_records:
        print("No performance data available yet.")
        return

    x_records = [
        record
        for record in all_records
        if record.get("data_source", "").strip().upper() == "X API"
    ]

    legacy_count = len(all_records) - len(x_records)

    print("\n--- RECOMMENDATION DATA SOURCE ---")
    print(f"Total performance records stored: {len(all_records)}")
    print(f"Real X API records used for recommendations: {len(x_records)}")
    print(f"Legacy/manual records excluded from recommendations: {legacy_count}")

    if not x_records:
        print(
            "\nNo X API performance records are available yet. "
            "Use Option 8 to retrieve live metrics from X."
        )
        return

    total_posts = len(x_records)

    avg_views = sum(r["views"] for r in x_records) / total_posts
    avg_likes = sum(r["likes"] for r in x_records) / total_posts
    avg_reposts = sum(r["reposts"] for r in x_records) / total_posts
    avg_replies = sum(r["replies"] for r in x_records) / total_posts
    avg_bookmarks = sum(r["bookmarks"] for r in x_records) / total_posts

    total_views = sum(r["views"] for r in x_records)
    total_engagement_actions = sum(
        r["likes"] + r["reposts"] + r["replies"] + r["bookmarks"]
        for r in x_records
    )

    if total_views > 0:
        observed_engagement_rate = (
            total_engagement_actions / total_views
        ) * 100
    else:
        observed_engagement_rate = 0

    print("\n--- REAL X PERFORMANCE ---")
    print(f"X API posts tracked: {total_posts}")
    print(f"Average views: {avg_views:.2f}")
    print(f"Average likes: {avg_likes:.2f}")
    print(f"Average reposts: {avg_reposts:.2f}")
    print(f"Average replies: {avg_replies:.2f}")
    print(f"Average bookmarks: {avg_bookmarks:.2f}")
    print(f"Observed engagement rate: {observed_engagement_rate:.2f}%")

    print("\n--- DATA CONFIDENCE ---")

    if total_posts < 5:
        print(
            "Very early sample. NEORUINS will report observations, "
            "but will not make strong strategy recommendations yet."
        )
        print("Next real-data goal: Track 5 X API posts.")
    elif total_posts < 10:
        print(
            "Early sample. Patterns can be used as testing signals, "
            "but more real posts are needed."
        )
        print("Next real-data goal: Track 10 X API posts.")
    else:
        print(
            "The real-X sample is large enough to begin comparing "
            "early content and schedule patterns."
        )

    print("\n--- REAL X POST TYPE DATA ---")

    post_types = [
        "Gaming Question",
        "Hot Take",
        "News Reaction",
        "Streaming Post",
        "Meme Style",
    ]

    types_with_data = 0

    for post_type in post_types:
        matching = [
            record
            for record in x_records
            if record["post_type"] == post_type
        ]

        if not matching:
            print(f"{post_type}: No real X data yet.")
            continue

        types_with_data += 1
        type_views = sum(r["views"] for r in matching)
        type_actions = sum(
            r["likes"] + r["reposts"] + r["replies"] + r["bookmarks"]
            for r in matching
        )

        type_rate = (type_actions / type_views * 100) if type_views > 0 else 0

        print(
            f"{post_type}: "
            f"{len(matching)} X API tracked | "
            f"Avg views: {type_views / len(matching):.2f} | "
            f"Observed engagement rate: {type_rate:.2f}%"
        )

    print("\n--- NEORUINS DATA-BASED GUIDANCE ---")

    if total_posts < 5:
        print(
            "Keep collecting real X metrics before changing your content "
            "strategy based on performance."
        )
    elif types_with_data < 2:
        print(
            "Collect real X data from at least one additional post type "
            "before comparing content formats."
        )
    else:
        type_summaries = []

        for post_type in post_types:
            matching = [
                record
                for record in x_records
                if record["post_type"] == post_type
            ]

            if len(matching) < 3:
                continue

            type_views = sum(r["views"] for r in matching)
            type_actions = sum(
                r["likes"] + r["reposts"] + r["replies"] + r["bookmarks"]
                for r in matching
            )
            rate = (type_actions / type_views * 100) if type_views > 0 else 0

            type_summaries.append({
                "post_type": post_type,
                "count": len(matching),
                "avg_views": type_views / len(matching),
                "engagement_rate": rate,
            })

        if not type_summaries:
            print(
                "There is real data across multiple post types, but NEORUINS "
                "needs at least 3 X API records for a post type before treating "
                "its results as a content-format testing signal."
            )
        else:
            type_summaries.sort(
                key=lambda item: (
                    item["engagement_rate"],
                    item["avg_views"],
                ),
                reverse=True,
            )

            top = type_summaries[0]

            print(
                f"{top['post_type']} currently has the strongest observed "
                f"engagement rate among post types with at least 3 real-X "
                f"records ({top['engagement_rate']:.2f}%)."
            )
            print(
                "Use that as a testing signal, not a guarantee, and keep "
                "collecting comparable posts."
            )

    print("\n--- RECENT VS EARLIER REAL X PERFORMANCE ---")

    dated_records = []

    for record in x_records:
        try:
            record_date = datetime.strptime(
                record["date_tracked"],
                "%Y-%m-%d %H:%M:%S",
            )
            dated_records.append((record_date, record))
        except ValueError:
            continue

    if len(dated_records) < 4:
        print(
            "Not enough real X records yet. Track at least 4 X API posts "
            "for a recent-vs-earlier comparison."
        )
        return

    dated_records.sort(key=lambda item: item[0])
    midpoint = len(dated_records) // 2

    earlier = [record for _, record in dated_records[:midpoint]]
    recent = [record for _, record in dated_records[midpoint:]]

    earlier_views = sum(r["views"] for r in earlier) / len(earlier)
    recent_views = sum(r["views"] for r in recent) / len(recent)

    def group_engagement_rate(group):
        views = sum(r["views"] for r in group)
        actions = sum(
            r["likes"] + r["reposts"] + r["replies"] + r["bookmarks"]
            for r in group
        )
        return (actions / views * 100) if views > 0 else 0

    earlier_rate = group_engagement_rate(earlier)
    recent_rate = group_engagement_rate(recent)

    print(f"Earlier real-X posts: {len(earlier)}")
    print(f"Recent real-X posts: {len(recent)}")
    print(f"\nEarlier average views: {earlier_views:.2f}")
    print(f"Recent average views: {recent_views:.2f}")
    print(f"\nEarlier observed engagement rate: {earlier_rate:.2f}%")
    print(f"Recent observed engagement rate: {recent_rate:.2f}%")

    print(
        "\nThis comparison describes your real X performance data over time; "
        "it does not establish that one period caused the other."
    )



def load_published_post_records():
    records = []

    if not PUBLISHED_FILE.exists():
        return records

    content = PUBLISHED_FILE.read_text(encoding="utf-8").strip()

    if not content:
        return records

    blocks = content.split("--- PUBLISHED POST ---")

    for block in blocks:
        if not block.strip():
            continue

        record = {
            "published_at": "",
            "account": "",
            "post_id": "",
            "post": "",
        }
        post_lines = []
        reading_post = False

        for line in block.splitlines():
            stripped = line.strip()

            if stripped.startswith("Published At:"):
                record["published_at"] = stripped.replace(
                    "Published At:", "", 1
                ).strip()
                reading_post = False
            elif stripped.startswith("Account:"):
                record["account"] = stripped.replace(
                    "Account:", "", 1
                ).strip()
                reading_post = False
            elif stripped.startswith("X Post ID:"):
                record["post_id"] = stripped.replace(
                    "X Post ID:", "", 1
                ).strip()
                reading_post = False
            elif stripped.startswith("Post:"):
                post_lines.append(stripped.replace("Post:", "", 1).strip())
                reading_post = True
            elif reading_post:
                post_lines.append(line)

        record["post"] = "\n".join(post_lines).strip()

        if record["post"]:
            records.append(record)

    return records


def find_published_record(post):
    target = post.strip()

    for record in load_published_post_records():
        if record["post"].strip() == target:
            return record

    return None


def published_time_for_performance(published_at):
    if not published_at:
        return ""

    try:
        parsed = datetime.strptime(published_at, "%Y-%m-%d %H:%M:%S")
        return parsed.strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return ""


def load_published_post_ids():
    published_ids = set()

    if not PUBLISHED_FILE.exists():
        return published_ids

    content = PUBLISHED_FILE.read_text(encoding="utf-8").strip()

    if not content:
        return published_ids

    for line in content.splitlines():
        if line.startswith("X Post ID:"):
            post_id = line.replace("X Post ID:", "", 1).strip()

            if post_id:
                published_ids.add(post_id)

    return published_ids


def load_published_post_texts():
    published_posts = set()

    if not PUBLISHED_FILE.exists():
        return published_posts

    content = PUBLISHED_FILE.read_text(encoding="utf-8").strip()

    if not content:
        return published_posts

    blocks = content.split("--- PUBLISHED POST ---")

    for block in blocks:
        if not block.strip():
            continue

        lines = block.splitlines()
        post_lines = []
        reading_post = False

        for line in lines:
            stripped = line.strip()

            if stripped.startswith("Post:"):
                post_lines.append(
                    stripped.replace("Post:", "", 1).strip()
                )
                reading_post = True
            elif reading_post:
                if stripped.startswith("Published At:") or stripped.startswith("X Post ID:"):
                    reading_post = False
                else:
                    post_lines.append(line)

        post = "\n".join(post_lines).strip()

        if post:
            published_posts.add(post)

    return published_posts


def record_published_post(post, post_id, username):
    with open(PUBLISHED_FILE, "a", encoding="utf-8") as file:
        file.write("\n--- PUBLISHED POST ---\n")
        file.write(
            f"Published At: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        file.write(f"Account: @{username}\n")
        file.write(f"X Post ID: {post_id}\n")
        file.write(f"Post: {post}\n")


def publish_to_x(post):
    """
    Publish one approved post to X only after explicit user confirmation.
    Successfully published posts are recorded so they are not offered again.
    """
    print("\n--- X PUBLISHING LAYER ---")
    print("Post prepared for X:")
    print(post)

    if not post.strip():
        print("\nERROR: The selected post is empty.")
        print("Nothing was published.")
        return False

    if post.strip() in load_published_post_texts():
        print("\nALREADY PUBLISHED: This post is in published_posts.txt.")
        print("Nothing was published again.")
        return False

    if len(post) > 280:
        print(f"\nERROR: This post is {len(post)} characters long.")
        print("X posts must be 280 characters or fewer for this bot.")
        print("Nothing was published.")
        return False

    load_dotenv()

    api_key = os.getenv("X_API_KEY")
    api_key_secret = os.getenv("X_API_KEY_SECRET")
    access_token = os.getenv("X_ACCESS_TOKEN")
    access_token_secret = os.getenv("X_ACCESS_TOKEN_SECRET")

    if not all([
        api_key,
        api_key_secret,
        access_token,
        access_token_secret,
    ]):
        print("\nERROR: One or more X credentials are missing from .env.")
        print("Nothing was published.")
        return False

    try:
        client = tweepy.Client(
            consumer_key=api_key,
            consumer_secret=api_key_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
        )

        account = client.get_me()

        if not account.data:
            print("\nERROR: X did not return account information.")
            print("Nothing was published.")
            return False

        username = account.data.username

        print(f"\nConnected account: @{username}")
        print("\nFINAL PREVIEW:")
        print(post)
        print("\nWARNING: Publishing will make this post public on X.")

        confirmation = input(
            'Type exactly "YES" to publish, or anything else to cancel: '
        ).strip()

        if confirmation != "YES":
            print("\nCANCELLED: Nothing was published.")
            return False

        response = client.create_tweet(text=post)

        if response.data:
            post_id = str(response.data["id"])
            record_published_post(post, post_id, username)

            print("\nSUCCESS: The post was published to X.")
            print(f"Post ID: {post_id}")
            print(f"Account: @{username}")
            print("Publication recorded in published_posts.txt.")
            return True

        print("\nERROR: X did not return post information.")
        print("Check your X account before trying again.")
        return False

    except tweepy.TweepyException as error:
        print("\nERROR: X API request failed.")
        print(error)
        print("Check your X account before retrying if the result is uncertain.")
        return False

def get_due_scheduled_drafts():
    drafts = load_drafts()
    due_drafts = []
    now = datetime.now()

    for index, draft in enumerate(drafts):
        scheduled_time = parse_schedule(draft.get("scheduled_for", ""))

        if scheduled_time is not None and scheduled_time <= now:
            due_drafts.append({
                "draft_index": index,
                "scheduled_time": scheduled_time,
                "draft": draft,
            })

    due_drafts.sort(key=lambda item: item["scheduled_time"])
    return drafts, due_drafts


def review_due_scheduled_posts():
    drafts, due_drafts = get_due_scheduled_drafts()

    if not due_drafts:
        print("\nNo scheduled posts are due for review.")
        return

    print("\n--- DUE SCHEDULED POSTS ---")

    for display_index, item in enumerate(due_drafts, start=1):
        draft = item["draft"]
        print(
            f"{display_index}. {draft['topic']} | "
            f"{draft['post_type']} | "
            f"{draft['scheduled_for']}"
        )

    selection = input(
        "\nChoose a due scheduled post to review "
        "(or 0 to cancel): "
    ).strip()

    if selection == "0":
        return

    if not selection.isdigit() or not 1 <= int(selection) <= len(due_drafts):
        print("Invalid selection.")
        return

    selected = due_drafts[int(selection) - 1]
    draft = selected["draft"]

    print("\n--- SCHEDULED POST REVIEW ---")
    print(f"Topic: {draft['topic']}")
    print(f"Post Type: {draft['post_type']}")
    print(f"Scheduled For: {draft['scheduled_for']}")
    print(f"Score: {draft['score']}")
    print("\nPOST:")
    print(draft["post"])

    show_quality_results(draft["post"])

    print("\nThis post is due, but it will NOT publish automatically.")
    print("The normal X publishing layer will still require exact YES confirmation.")

    action = input(
        "\nType P to continue to X publishing, or press Enter to cancel: "
    ).strip().upper()

    if action != "P":
        print("\nCANCELLED: The scheduled draft was kept.")
        return

    published = publish_to_x(draft["post"])

    if not published:
        print("\nThe scheduled draft was kept because publication was not confirmed successful.")
        return

    original_index = selected["draft_index"]

    if 0 <= original_index < len(drafts):
        drafts.pop(original_index)
        write_drafts(drafts)
        print("Scheduled draft removed after successful publication.")


def x_publishing_layer():
    while True:
        print("\n--- X PUBLISHING LAYER ---")
        print("1. Publish an Approved Post")
        print("2. Review Due Scheduled Posts")
        print("0. Return")

        choice = input("\nChoose an option: ").strip()

        if choice == "0":
            return

        if choice == "1":
            posts = load_approved_post_records()
            published_post_texts = load_published_post_texts()
            posts = [
                record
                for record in posts
                if record["post"].strip() not in published_post_texts
            ]

            if not posts:
                print("\nNo unpublished approved posts are ready for X.")
                print("Approved posts already recorded as published are hidden here.")
                continue

            print("\n--- APPROVED POSTS READY FOR X ---")

            for index, record in enumerate(posts, start=1):
                print(
                    f"{index}. {record['topic']} | "
                    f"{record['post_type']} | "
                    f"{record['date']}"
                )

            selection = input(
                "\nChoose an approved post to prepare for X "
                "(or 0 to cancel): "
            ).strip()

            if selection == "0":
                continue

            if not selection.isdigit() or not 1 <= int(selection) <= len(posts):
                print("Invalid selection.")
                continue

            selected_post = posts[int(selection) - 1]
            publish_to_x(selected_post["post"])

        elif choice == "2":
            review_due_scheduled_posts()

        else:
            print("Invalid choice. Please select 0-2.")


def show_startup_schedule_check():
    _, due_drafts = get_due_scheduled_drafts()

    print("\n--- SCHEDULE CHECK ---")

    if not due_drafts:
        print("No scheduled posts are due for review.")
        return

    count = len(due_drafts)
    word = "post" if count == 1 else "posts"

    print(f"You have {count} scheduled {word} due for review.")
    print("Use Option 21 -> Review Due Scheduled Posts.")


def main():
    show_startup_schedule_check()

    while True:
        print("\n==============================")
        print("       NEORUINS BOT")
        print("==============================")

        print("1. Generate New Post")
        print("2. View Approved Posts")
        print("3. View Content History")
        print("4. View Drafts")
        print("5. Review Drafts")
        print("6. Content Calendar")
        print("7. Manage Drafts")
        print("8. Track Post Performance")
        print("9. View Performance History")
        print("10. Performance Analytics")
        print("11. Post Type Analytics")
        print("12. Performance Insights")
        print("13. Posting Time Analytics")
        print("14. Posting Hour Analytics")
        print("15. Posting Hour Insights")
        print("16. Posting Day Analytics")
        print("17. Posting Day Insights")
        print("18. Posting Schedule Insights")
        print("19. Content Strategy Insights")
        print("20. Content Type + Schedule Insights")
        print("21. X Publishing Layer")
        print("22. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            generate_new_post()
        elif choice == "2":
            view_approved_posts()
        elif choice == "3":
            view_content_history()
        elif choice == "4":
            view_drafts()
        elif choice == "5":
            review_drafts()
        elif choice == "6":
            content_calendar()
        elif choice == "7":
            manage_drafts()
        elif choice == "8":
            track_post_performance()
        elif choice == "9":
            view_performance_history()
        elif choice == "10":
            performance_analytics()
        elif choice == "11":
            post_type_analytics()
        elif choice == "12":
            performance_insights()
        elif choice == "13":
            posting_time_analytics()
        elif choice == "14":
            posting_hour_analytics()
        elif choice == "15":
            posting_hour_insights()
        elif choice == "16":
            posting_day_analytics()
        elif choice == "17":
            posting_day_insights()
        elif choice == "18":
            posting_schedule_insights()
        elif choice == "19":
            content_strategy_insights()
        elif choice == "20":
            content_schedule_insights()
        elif choice == "21":
            x_publishing_layer()
        elif choice == "22":
            print("\nNEORUINS BOT SHUTTING DOWN...")
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-22.")


if __name__ == "__main__":
    main()
