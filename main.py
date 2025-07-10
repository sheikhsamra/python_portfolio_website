import streamlit as st

# Page config
st.set_page_config(page_title="Samra's Portfolio", page_icon="🎨", layout="wide")

# Custom CSS for styling and scrollbar colors
st.markdown("""
<style>
    /* Background and fonts */
    body, .main {
        background-color: #f7f9fc;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    h1, h2, h3 {
        color: #1f2937;
        font-weight: 700;
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #cecece;
        color: white;
        padding-top: 20px;
    }
     /* Sidebar Title (Navigation heading) */
section[data-testid="stSidebar"] h1 {
    color: Black;
    font-size: 1.6rem;
    font-weight: bold;
    }       

    [data-testid="stSidebar"] .css-1d391kg {
        color: white;
    }
    /* Sidebar active link */
    .css-1hynsf2 a {
        color: #d1d5db !important;
    }
    /* Button styling */
    .stButton>button {
        background-color: #4F46E5;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        border: none;
        font-weight: 600;
        cursor: pointer;
        transition: background-color 0.3s ease, box-shadow 0.3s ease;
        box-shadow: 0 3px 6px rgba(79, 70, 229, 0.4);
    }
    .stButton>button:hover {
        background-color: #3730a3;  /* Darker shade on hover */
        box-shadow: 0 6px 12px rgba(55, 48, 163, 0.6);
    }
    /* Input fields */
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        border-radius: 10px;
        padding: 10px;
        border: 1.5px solid #ddd;
        font-size: 1rem;
        transition: border-color 0.3s ease;
    }
    .stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus {
        border-color: #4F46E5;
        outline: none;
    }
    /* Link styling */
    a {
        color: #4F46E5;
        text-decoration: none;
        font-weight: 600;
        transition: color 0.3s ease;
    }
    a:hover {
        text-decoration: underline;
        color: #3730a3;
    }
    /* Contact social links */
    .social-links {
        margin-top: 1rem;
        font-size: 1.1rem;
    }
    .social-links a {
        margin-right: 1.5rem;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        color: #4F46E5;
        transition: color 0.3s ease;
    }
    .social-links a:hover {
        color: #3730a3;
        text-decoration: underline;
    }
    /* Simple icon style for social links */
    .social-icon {
        font-size: 1.3rem;
    }

    /* Projects images hover effect */
    .stImage > img {
        border-radius: 12px;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
    }
    .stImage > img:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(79, 70, 229, 0.4);
        cursor: pointer;
    }

    /* Project subheaders styling */
    .css-1v0mbdj h2, .css-1v0mbdj h3 {
        margin-top: 0.5rem;
        margin-bottom: 0.75rem;
        color: #3b4252;
    }

    /* Expander styling */
    .stExpander > div {
        border-radius: 10px;
        background-color: #fff;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        padding: 1rem;
        font-size: 0.95rem;
        color: #4a4a4a;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# ----- Home Page -----
if page == "Home":
    st.title("👩‍💻 Samra Moinuddin — The Creative Coder")
    st.subheader("Frontend Developer | Graphic Designer | Python Enthusiast")
    st.write("---")

    st.header("📌 About Me")
    st.write("""
Hello! I'm Samra, a passionate and creative frontend developer and graphic designer based in Pakistan.
I specialize in crafting elegant, user-friendly, and fully responsive websites that combine clean design with strong functionality.

With a solid foundation in HTML, CSS, Tailwind CSS, JavaScript, TypeScript, React.js, Next.js, and Python,
I enjoy transforming ideas into visually appealing digital experiences. I’m not just a developer — I bring a designer’s eye
for detail and a developer’s precision to every project I work on.

I’m currently expanding my skills by learning Agentic AI at Governor House and pursuing a Modern Web & App Development course at Saylani Mass IT Training Program.

Whether it's building a full-fledged e-commerce platform or designing a sleek personal portfolio,
my goal is always to deliver pixel-perfect, fast-loading, and accessible web solutions.

I'm also constantly learning and exploring new technologies to stay ahead in the ever-evolving world of web development.
""")
    st.image("about.jpeg", caption="Coding & Design Vibes", use_container_width=True)

# ----- Projects Page -----
elif page == "Projects":
    st.title("🧩 Projects Showcase")
    st.write("---")

    # First row - 3 columns
    cols1 = st.columns(3)

    with cols1[0]:
        st.image("Capture.PNG", caption="Marketplace Builder", use_container_width=True)
        st.subheader("🛒 Marketplace Builder")
        with st.expander("Description here"):
            st.write("""
    A responsive e-commerce clothing marketplace built using **Next.js**, **Tailwind CSS**, and **Sanity CMS**.  
    The platform supports full product management, payment, and order tracking.
    
    **Key Features:**
    - 🔗 Integrated with **Sanity** for real-time product data via API
    - 💳 **Stripe** payment gateway for secure checkout
    - 📦 Orders are saved and managed through **Sanity**
    - ⚡ Built with **Next.js** for fast performance and SEO
    - 📱 Fully **responsive** using Tailwind CSS
    
    Developed with a focus on performance, design, and user experience.
    """, unsafe_allow_html=True)
            st.markdown("[🌐 Visit Website](https://marketplace-builder-hackathon-two.vercel.app/)", unsafe_allow_html=True)

    with cols1[1]:
        st.image("Capture2.PNG", caption="SM Collections", use_container_width=True)
        st.subheader("🛍️ SM Collections")
        with st.expander("Description here"):
            st.write("""
    A stylish and fully responsive **clothing brand website** built using **HTML**, **CSS**, and **JavaScript** — no frameworks used!

    **Key Features:**
    - 🎨 Custom-designed using only **CSS** for layout and styling
    - 📱 Fully **responsive** design for mobile, tablet, and desktop
    - 🧥 Showcases categories like **Men’s**, **Women’s**, and **Kids’** collections
    - 🖼️ Beautiful image galleries and hover effects
    - 🔗 Simple, clean UI for a modern shopping experience

    Perfect for small fashion brands or product showcases with lightweight performance.

    """, unsafe_allow_html=True)
            st.markdown("[🌐 Visit Website](https://sm-collections-website-with-css.vercel.app/)", unsafe_allow_html=True)

    with cols1[2]:
        st.image("Capture3.PNG", caption="SM Blog Website", use_container_width=True)
        st.subheader("📝 SM Blog Website")
        with st.expander("Description here"):
            st.write("""
        A modern, dynamic **blog website** built with **Next.js** that fetches content via API for seamless updates.

        **Features include:**
        - 🔄 Dynamic content fetching for real-time blog updates
        - 🧑‍💻 Easy-to-manage posts and categories
        - 💬 Comment system allowing users to **add, edit, and delete comments** on each blog post
        - 🌐 Fast and SEO-friendly with server-side rendering
        - 📱 Fully responsive design for smooth reading on any device
        - 💬 Clean and intuitive user interface to enhance reader engagement

        Perfect for bloggers, writers, or content creators looking to share their stories with a professional, scalable platform.
        """)
            st.markdown("[🌐 Visit Website](https://sm-blog-website.vercel.app/)", unsafe_allow_html=True)

    # Second row - next 3 projects
    cols3 = st.columns(3)

    with cols3[0]:
        st.image("Capture7.PNG", caption="SM Personal Library Management", use_container_width=True)
        st.subheader("Personal Library Management")
        with st.expander("📋 Description"):
            st.write(""" The SM Personal Library Management System is a modern, user-friendly Python application developed using Streamlit. It allows users to efficiently manage their personal book collection in a digital format.

🔑 Key Features:
➕ Add Books: Seamlessly add books with relevant details like title and author.

❌ Remove Books: Delete books from your personal library when no longer needed.

✅ Mark as Read/Unread: Track your reading progress by marking books as read or unread.

🔍 Search Books: Quickly find specific books using the built-in search functionality.

📊 View Library Statistics: Get real-time insights into your reading habits, including the number of books read, unread, and total entries.

🖥️ Interactive Interface: Clean, responsive UI built with Streamlit for a smooth user experience.

This project reflects your skills in Python, Streamlit, and data handling, offering a practical and elegant solution for book lovers to manage and monitor their reading journey. """)
        st.markdown("[🌐 Visit Website](https://python-project4-lms.streamlit.app/)")

    with cols3[1]:
        st.image("Capture10.PNG", caption="SM Password Strength Meter", use_container_width=True)
        st.subheader("Password Strength Meter")
        with st.expander("📋 Description"):
            st.write(""" The SM Password Strength Meter is a Streamlit-based Python application designed to help users create strong and secure passwords by evaluating their strength in real-time.

🚀 Key Features:
✅ Instant Password Evaluation: Checks the strength of your password as you type (Weak, Moderate, Strong).

🔍 Security Criteria Analysis:

Length of password

Use of uppercase and lowercase letters

Inclusion of numbers

Use of special characters

🛡️ Visual Feedback with color indicators and status messages.

📱 User-Friendly Interface using Streamlit, styled with custom CSS for a clean and modern UI.

🎯 Perfect for personal use or integrating into larger authentication systems.

This project showcases your Python programming, logic building, and UI/UX design skills using Streamlit — a fast and effective tool for deploying Python apps. """)
        st.markdown("[🌐 Visit Website](https://sm-python-password-strength-meter.streamlit.app/)")

    with cols3[2]:
        st.image("Capture9.PNG", caption="SM Unit Converter", use_container_width=True)
        st.subheader("Unit Converter")
        with st.expander("📋 Description"):
            st.write(""" The SM Unit Converter is a simple yet powerful web application built with Python and Streamlit, designed to perform fast and accurate unit conversions across multiple categories.

🔧 Key Features:
📏 Length: Convert between meters, kilometers, miles, feet, and more.

⚖️ Weight: Easily switch between kilograms, grams, pounds, and ounces.

⏱️ Time: Convert hours, minutes, and seconds with precision.

🌡️ Temperature: Switch between Celsius, Fahrenheit, and Kelvin.

🧮 Area: Convert area units like square kilometers to square miles and vice versa.

🔁 Bi-directional Conversions: Includes conversions like:

Kilometers ↔️ Miles

Miles ↔️ Kilometers

This project showcases your ability to create a responsive, interactive, and multi-functional web tool using Python and Streamlit, ideal for daily use by students, professionals, and anyone needing quick and accurate conversions. """)
        st.markdown("[🌐 Visit Website](https://sm-python-unit-converter.streamlit.app/)")

# ----- Contact Page -----
if page == "Contact":
    st.title("📬 Contact Me")
    st.write("Feel free to get in touch by filling out the form below.")
    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")

        if submitted:
            if name and email and message:
                st.success(f"Thanks {name}! I'll get back to you soon.")
            else:
                st.error("Please fill in all fields before submitting.")

    # Social links with emojis/icons
    st.markdown("""
    <div class="social-links">
        <a href="https://www.linkedin.com/in/samra-moinuddin-7164142b6/?originalSubdomain=pk" target="_blank" rel="noopener noreferrer">
            <span class="social-icon">🔗</span> LinkedIn
        </a>
        <a href="https://github.com/sheikhsamra" target="_blank" rel="noopener noreferrer">
            <span class="social-icon">🐱</span> GitHub
        </a>
        <a href="#" >📧 shaikhsamra855@gamil.com</a>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")
    st.caption("© 2025 Samra Moinuddin. All rights reserved.")
