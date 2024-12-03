import streamlit as st

def add_custom_css():
    st.markdown("""
        <style>
        /* General Background */
        body {
            background-color: #F5F5F5; /* Light grey background */
        }
        .stApp {
            background-color: #F5F5F5; /* Main container in light grey */
        }
        /* Header Text */
        h1, h2, h3, h4, h5 {
            font-family: 'Georgia', serif; /* Magical Academic Feel */
            color: #002D72 !important; /* Wharton Navy Blue for headers */
        }
        /* Body Text */
        p, div, label, span, li {
            font-family: 'Verdana', sans-serif; /* Clean and Readable */
            color: #002D72 !important; /* Navy Blue for body content */
        }
        /* Static Button Styling */
        .stButton>button {
            background-color: #af0c0c !important; /* Gryffindor Red */
            color: #FFFFFF !important; /* White text for readability */
            border: 2px solid #FFD700 !important; /* Gold border */
            border-radius: 8px; /* Rounded corners */
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

# Apply custom CSS
add_custom_css()

# Define the path to the avatar folder
avatar_folder = "https://github.com/mcarolyn334/Coding-Projects-2024/raw/main/"

# Map personality names to their corresponding avatar files
avatar_files = {
    "Harry Potter": f"{avatar_folder}Potter.webp",
    "Draco Malfoy": f"{avatar_folder}Malfoy.webp",
    "Cedric Diggory": f"{avatar_folder}Cedric.webp",
    "Albus Dumbledore": f"{avatar_folder}Dumbledore.webp",
    "Cho Chang": f"{avatar_folder}Cho.webp",
    "Hermione Granger": f"{avatar_folder}Hermione.webp"
}

# Define questions and responses
questions = [
    # Harry Potter (Pie Expander)
    {"text": "You’re negotiating with a potion-making shop to co-develop a revolutionary magical brew—think self-refilling Butterbeer. Your team of brewers is stretched thin, and the shop insists on keeping the potion recipe exclusive. But you’ve just had a lightbulb moment: pooling resources could help perfect the potion faster and beat your competitors to Diagon Alley shelves. Do you:",
     "options": [
         ("Propose co-ownership and frame it as a win-win for both parties.", "Harry Potter"),
         ("Let them keep the recipe but secure a hefty percentage of the profits.", "Albus Dumbledore"),
         ("Demand full ownership—it’s your potion concept!", "Draco Malfoy"),
         ("Keep your idea to yourself for now, hoping they’ll budge later.", "Cho Chang")
     ]},
    {"text": "Your broom supplier just asked for a 15% price increase, citing high-quality bristle shortages. Upon investigation, you discover they could cut costs with a spell upgrade—but they'd need some upfront funding. They're hesitant to gamble. Do you:",
     "options": [
         ("Offer to share the cost and reap mutual benefits.", "Harry Potter"),
         ("Negotiate the increase down and let them figure out the upgrade themselves.", "Cho Chang"),
         ("Push for a fixed-price deal and tell them to deal with the bristle shortage.", "Draco Malfoy"),
         ("Wait for them to suggest the process change themselves.", "Cedric Diggory")
     ]},
    {"text": "I enjoy discovering shared interests and crafting solutions that satisfy both sides.",
     "options": [
         ("Strongly Disagree", "Draco Malfoy"),
         ("Disagree", "Albus Dumbledore"),
         ("Neutral", "Cho Chang"),
         ("Agree", "Harry Potter"),
         ("Strongly Agree", "Harry Potter")
     ]},

    # Draco Malfoy (Challenger)
    {"text": "You’re negotiating with a wandmaker who thinks they hold all the power. They want extra Galleons for a faster delivery, but you know they can manage it without the extra cost—because you've done your homework. Do you:",
     "options": [
         ("Lay out your research confidently and demand they stick to the original agreement.", "Draco Malfoy"),
         ("Offer a bonus but secure better long-term terms.", "Harry Potter"),
         ("Agree to the extra cost, because time is of the essence.", "Cedric Diggory"),
         ("Drop subtle hints about their competition to turn up the heat.", "Cho Chang")
     ]},
    {"text": "A brilliant young witch is demanding a ridiculous salary to join your potion development team—think ‘buy a dragon egg’ expensive. She claims to have another offer on the table, but you’re 80% sure it’s a bluff. Do you:",
     "options": [
         ("Call her bluff and stick to the market rate.", "Draco Malfoy"),
         ("Offer her a leadership role to sweeten the deal without breaking the Gringotts vault.", "Cedric Diggory"),
         ("Agree to her demands and remind yourself it's a long-term investment.", "Harry Potter"),
         ("Push back slightly while highlighting the non-financial benefits of joining your team.", "Albus Dumbledore")
     ]},
    {"text": "I believe in driving tough bargains to ensure the best outcomes for myself or my team.",
     "options": [
         ("Strongly Disagree", "Cedric Diggory"),
         ("Disagree", "Albus Dumbledore"),
         ("Neutral", "Harry Potter"),
         ("Agree", "Draco Malfoy"),
         ("Strongly Agree", "Draco Malfoy")
     ]},

    # Cedric Diggory (Harmonizer)
    {"text": "You’re meeting with a long-term supplier of dragon-hide gloves who values tradition. They’ve sent a junior goblin who won't make eye contact when you mention pricing. Meanwhile, your assistant is urgently sending owl messages saying 'we need this deal TODAY!' Do you:",
     "options": [
         ("Charm the junior goblin over lunch to understand their concerns.", "Cedric Diggory"),
         ("Request a meeting with a senior goblin to discuss matters more directly.", "Cho Chang"),
         ("Focus solely on pricing—your assistant needs this deal quickly.", "Draco Malfoy"),
         ("Suggest a group meeting to get everyone's cards on the table.", "Harry Potter")
     ]},
    {"text": "Your best client, Flourish and Blotts, is furious about a delayed delivery of enchanted quills and sends you an owl that simply says: 'Switching to another supplier—BYE.' Their business is crucial to you. Do you:",
     "options": [
         ("Apologize profusely and offer them free upgrades or future discounts.", "Cedric Diggory"),
         ("Provide a personalized solution without offering costly extras.", "Harry Potter"),
         ("Remind them of your long-standing, excellent service and their contract terms.", "Draco Malfoy"),
         ("Offer to review their account together to find a mutually beneficial solution.", "Cho Chang")
     ]},
    {"text": "I prioritize maintaining strong relationships over winning every negotiation point.",
     "options": [
         ("Strongly Disagree", "Draco Malfoy"),
         ("Disagree", "Cho Chang"),
         ("Neutral", "Albus Dumbledore"),
         ("Agree", "Cedric Diggory"),
         ("Strongly Agree", "Cedric Diggory")
     ]},

    # Albus Dumbledore (Visionary)
    {"text": "You’re pitching a new magical education program to the Hogwarts Board of Governors. Half of them are nodding, while one seems skeptical (likely thinking about the budget). Do you:",
     "options": [
         ("Dazzle them with visions of how this will benefit future wizards and witches.", "Albus Dumbledore"),
         ("Present detailed calculations showing long-term benefits.", "Cho Chang"),
         ("Focus on the public relations benefits—imagine Hogwarts in the Daily Prophet as a trailblazer.", "Harry Potter"),
         ("Address the skeptical governor directly to alleviate their concerns.", "Cedric Diggory")
     ]},
    {"text": "During a merger discussion between two magical businesses, the debate over whose logo will be on the new broomstick model becomes heated. The CEOs seem to be holding back their thoughts. Do you:",
     "options": [
         ("Shift the discussion to strategic goals and suggest logos can be addressed later.", "Albus Dumbledore"),
         ("Propose a temporary compromise: two logos for now, one mission.", "Harry Potter"),
         ("Suggest the CEOs have a private discussion to resolve it quietly.", "Cedric Diggory"),
         ("Gently remind everyone that logos won't matter if the deal doesn’t succeed.", "Cho Chang")
     ]},
    {"text": "I often lead negotiations by emphasizing long-term goals and a shared vision.",
     "options": [
         ("Strongly Disagree", "Draco Malfoy"),
         ("Disagree", "Harry Potter"),
         ("Neutral", "Cho Chang"),
         ("Agree", "Albus Dumbledore"),
         ("Strongly Agree", "Albus Dumbledore")
     ]},

    # Cho Chang (Strategist)
    {"text": "Your French partner from Beauxbatons wants to launch a new enchanted perfume right away but overlooked the Ministry's long approval process (which takes months). Your legal team's disapproving looks say it all. Do you:",
     "options": [
         ("Break out your well-prepared plan with contingencies.", "Cho Chang"),
         ("Agree to launch, then worry about the approvals later.", "Harry Potter"),
         ("Leave compliance to them—they know their country’s rules better.", "Cedric Diggory"),
         ("Suggest phased rollouts to minimize risk while still moving forward.", "Albus Dumbledore")
     ]},
    {"text": "A new supplier has sent you a contract thicker than 'Magical Drafts and Potions.' The clock is ticking, and your legal team murmurs about potential traps. Do you:",
     "options": [
         ("Postpone until you’ve analyzed every clause—you won’t sign without full understanding.", "Cho Chang"),
         ("Focus on the major issues and highlight areas that need clarification.", "Harry Potter"),
         ("Trust the supplier’s reputation but monitor carefully for any surprises.", "Cedric Diggory"),
         ("Propose a simpler, shorter contract to save time.", "Draco Malfoy")
     ]},
    {"text": "I rely on data and structured approaches to guide my negotiations.",
     "options": [
         ("Strongly Disagree", "Cedric Diggory"),
         ("Disagree", "Draco Malfoy"),
         ("Neutral", "Harry Potter"),
         ("Agree", "Cho Chang"),
         ("Strongly Agree", "Cho Chang")
     ]},

    # Hermione Granger (Ethicist)
    {"text": "During a deal for enchanted cauldrons, you find out that the cauldrons are being made by exploiting house-elf labor. The supplier is offering you the best deal in the market, but your conscience is unsettled. Do you:",
     "options": [
         ("Refuse to proceed until they improve conditions for the house-elves.", "Hermione Granger"),
         ("Use the information to negotiate a more favorable price.", "Draco Malfoy"),
         ("Proceed with the deal but keep tabs to revisit the issue later.", "Cho Chang"),
         ("Propose a solution that improves conditions while maintaining the deal.", "Cedric Diggory")
     ]},
    {"text": "You’re finalizing a licensing deal for a spell, and the other party slips in a vague ‘revenue-sharing agreement TBD’ clause. They insist it’s just a formality. Your legal team disagrees. Do you:",
     "options": [
         ("Refuse to sign until every clause is clarified.", "Hermione Granger"),
         ("Agree but add a renegotiation clause for safety.", "Cho Chang"),
         ("Sign, but plan to monitor and clarify later.", "Harry Potter"),
         ("Push back for a concrete deadline to finalize specifics.", "Draco Malfoy")
     ]},
    {"text": "I value ethical practices and fairness over short-term wins in negotiations.",
     "options": [
         ("Strongly Disagree", "Draco Malfoy"),
         ("Disagree", "Cho Chang"),
         ("Neutral", "Harry Potter"),
         ("Agree", "Hermione Granger"),
         ("Strongly Agree", "Hermione Granger")
     ]}
]

# Define detailed personality analysis
personality_analysis = {
    "Harry Potter": {
        "name": "Harry Potter (The Pie Expander)",
        "description": """Like Harry Potter, you believe in creating opportunities for everyone. You thrive in situations where cooperation and a sense of shared mission can lead to a bigger win for all. 
        Just like Harry’s willingness to put others first and see the best in people, you are a champion of win-win scenarios, even when times get tough.""",
        "strengths": """You have an unshakeable sense of fairness and are great at fostering collaboration. You inspire others to work together and can turn an adversary into an ally with genuine empathy. 
        You don’t just look to win—you look to grow the opportunity for everyone involved.""",
        "weaknesses": """Sometimes, your desire to make sure everyone benefits can lead to sacrifices on your end. You might overcompromise, risking your interests for the greater good, just as Harry sometimes puts himself at risk for others.""",
        "tips": """Stay focused on value creation, but don't be afraid to assert your needs—sometimes, you deserve a bigger piece of the pie too! Use Harry's tactic of gathering allies—like he did with Dumbledore's Army—and make sure you have a solid BATNA before making concessions. This will help balance cooperation with securing your own objectives.""",
        "secret_sauce": """Your secret sauce is **inspiring loyalty and leveraging collective strength**. Harry always found ways to bring others into the fold, making the solution stronger together. In negotiations, your natural ability to create a shared vision is what brings true, long-term success."""
    },
    "Draco Malfoy": {
        "name": "Draco Malfoy (The Challenger)",
        "description": """Like Draco Malfoy, you’re assertive and know how to leverage power. You’re not afraid to be direct and make demands. Draco’s confidence (sometimes arrogance) allows him to command attention in negotiations, and you carry that same boldness.""",
        "strengths": """You excel at setting high anchors and leveraging your position. You’re confident, decisive, and willing to push for the best possible outcome without hesitation. You understand the dynamics of power well, just like Draco does when navigating the complex politics of the wizarding world.""",
        "weaknesses": """Sometimes your approach can be too forceful, potentially alienating others or causing them to become defensive. Draco’s unwillingness to consider others’ needs often backfires, and the same can happen in negotiations if your focus on winning becomes too one-sided.""",
        "tips": """Channel Draco’s determination but soften your approach. Balance assertiveness with genuine curiosity about the other party’s perspective—sometimes yielding on smaller points can lead to greater overall gains. Consider blending a touch of empathy with your direct style to avoid unnecessary conflicts.""",
        "secret_sauce": """Your secret sauce is **fearless anchoring and strategic positioning**. Draco always knew how to set the tone and establish dominance early. When used effectively, your ability to confidently anchor negotiations can lead to favorable outcomes, as long as you’re careful not to burn bridges."""
    },
    "Cedric Diggory": {
        "name": "Cedric Diggory (The Harmonizer)",
        "description": """Like Cedric Diggory, you value relationships and fairness. Cedric was admired for his integrity and kindness, and you bring people together by ensuring everyone feels valued. 
        Cedric’s willingness to help Harry in the Triwizard Tournament reflects your approach: mutual respect and collaboration are key.""",
        "strengths": """You are empathetic, fair, and excellent at building trust. Like Cedric, you rally people towards shared goals, using charm to diffuse tension and create a cooperative environment.""",
        "weaknesses": """Your desire for harmony can lead to avoiding conflict, potentially sacrificing your own goals. Cedric sometimes held back to keep things fair, and you may face similar challenges by prioritizing group needs.""",
        "tips": """Assert your needs—speaking up doesn’t mean sacrificing harmony. Use “conditional agreements” to balance fairness with your interests. Be firm when needed while still preserving relationships.""",
        "secret_sauce": """Your secret sauce is **inspiring trust through fairness**. Like Cedric, your loyalty and sense of justice bring people together, fostering cooperation even in challenging negotiations."""
    },
    "Albus Dumbledore": {
        "name": "Albus Dumbledore (The Visionary)",
        "description": """Like Albus Dumbledore, you see the bigger picture and understand how to frame situations around shared values and long-term objectives. You’re an inspiring negotiator, always aiming to lead people toward a greater good, just as Dumbledore did with the Order of the Phoenix.""",
        "strengths": """You’re persuasive and excellent at motivating others to buy into your vision. You’re adept at reframing discussions to focus on shared goals, which helps in rallying people behind a common cause. Dumbledore’s focus on uniting everyone against a common enemy is mirrored in your negotiation style.""",
        "weaknesses": """You can get so caught up in your vision that you overlook practical concerns. Sometimes Dumbledore’s lofty plans missed the immediate needs of others, and similarly, your grand ideas can occasionally cause you to miss the details.""",
        "tips": """Remember to bring in specifics and concrete data to support your vision—this will help others feel confident in your plan. Use tactical empathy like Dumbledore did—understanding others’ concerns while guiding them toward your vision will strengthen your position.""",
        "secret_sauce": """Your secret sauce is **framing the negotiation around a compelling future**. Just like Dumbledore, you can get people to believe in a vision beyond themselves. This ability to inspire and unite makes you exceptionally powerful in negotiations that require buy-in and cooperation."""
    },
    "Cho Chang": {
        "name": "Cho Chang (The Strategist)",
        "description": """Like Cho Chang, you approach situations with a strategic mindset. Cho's intelligence and thoughtfulness are clear throughout her journey at Hogwarts, especially in her decisions regarding Dumbledore's Army and her cautious navigation of relationships. 
        You value being prepared and thinking ahead, ensuring that every move you make is well-calculated.""",
        "strengths": """You are analytical, methodical, and strategic in your approach. Like Cho, you consider different perspectives and prepare thoroughly before making decisions. You can assess the complexities of a negotiation, understand potential outcomes, and adjust accordingly, which makes you effective in dealing with intricate scenarios.""",
        "weaknesses": """Your focus on planning and analyzing can sometimes lead to hesitation or second-guessing yourself. Like Cho, who at times struggled with balancing emotions and making decisions, you may find that overthinking can hold you back from acting swiftly.""",
        "tips": """Trust your preparations, but remember to stay flexible—sometimes you need to act decisively without overanalyzing every aspect. Take a cue from Cho's willingness to stand up for what she believes in, even when it's difficult. Balance your strategic mindset with confident, timely actions to achieve your goals.""",
        "secret_sauce": """Your secret sauce is **your ability to stay calm under pressure and think strategically about the bigger picture**. Like Cho, you are capable of understanding the dynamics of a situation deeply, and this insight helps you negotiate with foresight and clarity, giving you an edge in complex negotiations."""
    },
    "Hermione Granger": {
        "name": "Hermione Granger (The Ethicist)",
        "description": """Like Hermione Granger, you hold a strong moral compass and believe that negotiations should be fair for everyone involved. You stand by your principles, even if it makes the process more challenging. Hermione’s pursuit of justice—whether in defending house-elves or fighting Voldemort—embodies your value-driven negotiation style.""",
        "strengths": """You’re highly principled, trustworthy, and respected for your integrity. You work to ensure that everyone is treated fairly, which builds credibility and trust in your negotiations. Hermione’s relentless dedication to doing the right thing ensures people can always rely on her.""",
        "weaknesses": """Sometimes, your strong ethical stance can make you seem rigid or unwilling to compromise. Just like Hermione’s strict adherence to rules sometimes caused friction, you might struggle to find flexibility when the situation demands it.""",
        "tips": """Identify which values are non-negotiable and where you can allow some leeway. Frame ethical stances in terms of benefits to the other party—help them see why doing the right thing works in their favor too. Use Hermione’s research skills to back up your ethical stances with data that supports their value.""",
        "secret_sauce": """Your secret sauce is **unwavering integrity combined with intelligence**. Like Hermione, you use your principles as both a guiding light and a negotiation tool, building trust and securing deals that stand the test of time because they’re built on a foundation of fairness and respect."""
    }
}
# Initialize session state variables
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "scores" not in st.session_state:
    st.session_state.scores = {personality: 0 for personality in avatar_files.keys()}
if "proceed" not in st.session_state:
    st.session_state.proceed = False

# Function to reset the quiz
def reset_quiz():
    st.session_state.current_question = 0
    st.session_state.scores = {personality: 0 for personality in avatar_files.keys()}
    st.session_state.proceed = False
    st.experimental_rerun()

# Run the quiz
def run_quiz():
    # Landing page
    if st.session_state.current_question == 0:
        st.title("Negotiation Personality Quiz: What Kind of HogWharton Dealmaker Are You?")
        st.write("""
            Negotiation is like a HogWharton elective you can't avoid—whether you're dealing with a potion master or trying to get discounted Fight Night tickets. 
            It’s all about how you wield your magic: the confident wand flourish, the perfectly timed pause, or the practiced smile that says, 'I’ve got this.' 
            But what kind of wizarding negotiator are you?

            Are you like Harry Potter, expanding the pie for everyone to win? Or maybe you're Draco Malfoy, pushing for the best outcome while trying not to look like an ass at Follies. 
            Perhaps you're Cedric Diggory, the harmonizer who keeps everyone happy, or Cho Chang, always three steps ahead. 
            This quiz will help you discover your inner wizarding dealmaker so the next time you're splitting a bill at The Three Broomsticks or negotiating with goblins at Gringotts, 
            you’ll know exactly which strengths to leverage.

            Ready to find out what kind of magical negotiator you are? Click 'Let’s Begin' and let the magic unfold!
        """)

        if st.button("Let's Begin"):
            st.session_state.current_question = 1
            st.experimental_rerun()

    # Quiz questions
    elif 1 <= st.session_state.current_question <= len(questions):
        current_question_index = st.session_state.current_question - 1
        current_question = questions[current_question_index]

        # Display progress
        st.progress(st.session_state.current_question / len(questions))
        st.write(f"Question {st.session_state.current_question} of {len(questions)}")
        st.write(f"**{current_question['text']}**")

        # Option selection
        selected_option = st.radio(
            "Choose your response:",
            [option[0] for option in current_question["options"]],
            key=f"response_{current_question_index}",
        )

        # Next button logic
        if st.button("Next"):
            if selected_option:
                for option in current_question["options"]:
                    if selected_option == option[0]:
                        st.session_state.scores[option[1]] += 1

                st.session_state.current_question += 1
                st.experimental_rerun()
            else:
                st.warning("Please select an option before proceeding!")

    # Results page
    else:
        st.subheader("Results")
        primary = max(st.session_state.scores, key=st.session_state.scores.get)

        st.image(avatar_files[primary], caption=f"{primary}", width=300)
        st.write(f"**Primary Personality: {primary}**")
        st.markdown(f"<i>{personality_analysis[primary]['description']}</i>", unsafe_allow_html=True)
        st.write(f"**Strengths**: {personality_analysis[primary]['strengths']}")
        st.write(f"**Weaknesses**: {personality_analysis[primary]['weaknesses']}")
        st.write(f"**Tips**: {personality_analysis[primary]['tips']}")
        st.write(f"**Secret Sauce**: {personality_analysis[primary]['secret_sauce']}")

        # Restart button
        if st.button("Take the Quiz Again"):
            reset_quiz()

# Call the quiz function
run_quiz()
