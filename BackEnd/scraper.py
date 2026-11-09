# -*- coding: utf-8 -*-
import winreg
from urllib.parse import unquote

# =================================================================
#                  PROTOCOL HANDLER REGISTRATION (winbo://)
# =================================================================
def register_custom_protocol():
    """ثبت پروتکل winbo:// در رجیستری ویندوز برای امکان اجرا مستقیم از مرورگر وب"""
    if platform.system() != "Windows":
        return
    try:
        python_exe = sys.executable
        if getattr(sys, 'frozen', False):
            # اگر برنامه به EXE تبدیل شده باشد
            executable_path = f'"{sys.executable}" "%1"'
        else:
            # اگر فایل پایتون مستقیم اجرا شود
            script_path = os.path.abspath(__file__)
            executable_path = f'"{python_exe}" "{script_path}" "%1"'

        # ایجاد کلید اصلی رجیستری برای winbo://
        # ایجاد کلید اصلی رجیستری برای winbo:// و tajerbam://
        key_path = r"Software\Classes\tajerbam"
        with winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path) as key:
            winreg.SetValue(key, "", winreg.REG_SZ, "URL:Tajerbam Scraper Protocol")
            winreg.SetValueEx(key, "URL Protocol", 0, winreg.REG_SZ, "")
            
            with winreg.CreateKey(key, r"shell\open\command") as command_key:
                winreg.SetValue(command_key, "", winreg.REG_SZ, executable_path)
                
        print("✅ پروتکل اختصاصی tajerbam:// با موفقیت در رجیستری ویندوز ثبت شد.")
    except Exception as e:
        print(f"⚠️ خطا در ثبت پروتکل رجیستری: {e}")

def parse_deeplink_args():
    """بررسی و پردازش پارامترهای ورودی از مرورگر (مثال: tajerbam://launch?token=...&keyword=...)"""
    parsed_params = {}
    if len(sys.argv) > 1:
        raw_url = sys.argv[1]
        if raw_url.startswith("tajerbam://") or raw_url.startswith("winbo://"):
            try:
                clean_url = raw_url.replace("tajerbam://", "").replace("winbo://", "").strip()
                if "?" in clean_url:
                    query_str = clean_url.split("?", 1)[1]
                    for param in query_str.split("&"):
                        if "=" in param:
                            k, v = param.split("=", 1)
                            parsed_params[k] = unquote(v)
            except Exception as e:
                print(f"Error parsing deep link: {e}")
    return parsed_params

"""
=============================================================================
   اسکرپر تاجربام - TAJERBAM SCRAPER ULTIMATE EDITION
   COPYRIGHT (C) 2026 TAJERBAM TEAM. ALL RIGHTS RESERVED.
=============================================================================
"""

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import threading
import sqlite3
import pymysql
import os
import sys
import time
import random
import re
import urllib.parse
import json
import socket
import subprocess
import requests
import asyncio
import logging
import hashlib
import base64
import webbrowser
import platform
import uuid
import requests
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Union, Tuple
from urllib.parse import quote, urljoin, urlparse, parse_qs 
from PIL import Image
import http.server
import socketserver

# --- Selenium Libraries (اضافه شده برای رفع قطعی مشکل مرورگر) ---
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# --- Data Analysis Libraries ---
try:
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    import pandas as pd
    import openpyxl
    DATA_ANALYSIS_AVAILABLE = True
    plt.rcParams['font.family'] = ['Vazir', 'Tahoma', 'Segoe UI', 'vazir', 'sans-serif']
except ImportError:
    DATA_ANALYSIS_AVAILABLE = False

# [اصلاح شماره ۱]: تعریف اولیه متغیر برای جلوگیری از NameError
BIDI_AVAILABLE = False

# --- Persian Font Fix Libraries (Matplotlib) ---
try:
    import arabic_reshaper
    from bidi.algorithm import get_display
    BIDI_AVAILABLE = True
except ImportError:
    ChromeDriverManager = None

# --- AI (G4F) ---
try:
    import g4f
    from g4f.client import Client as G4FClient
    AI_AVAILABLE = True
except ImportError:
    AI_AVAILABLE = False

# --- Jalali Date Support (Auto-Install) ---
try:
    import jdatetime
    JALALI_AVAILABLE = True
except ImportError:
    try:
        print("⏳ در حال نصب خودکار ماژول تقویم شمسی (jdatetime)...")
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "jdatetime"])
        import jdatetime
        JALALI_AVAILABLE = True
        print("✅ ماژول تقویم با موفقیت نصب شد! برنامه را دوباره اجرا کنید.")
    except Exception as e:
        print(f"❌ خطا در نصب خودکار تقویم: {e}")
        JALALI_AVAILABLE = False

# =================================================================
#                  MODULE 10: CONTENT FACTORY (PREMIUM EDITION)
# =================================================================
class ContentFactoryFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=THEME["bg_root"])
        self.current_project_id = None
        self.projects = []
        self.plan_data = []
        self.STATUS_COLORS = {
            "💡 ایده‌پردازی": "#607D8B", 
            "🎥 در حال تولید": "#FF9800", 
            "✂️ در حال تدوین": "#03A9F4", 
            "⏳ آماده انتشار": "#9C27B0", 
            "✅ منتشر شد": "#00E676"
        }
        self.init_db()
        self.build_ui()
        self.load_projects()

    def init_db(self):
        """ایجاد جداول و بروزرسانی هوشمند ستون‌های جدید برای نسخه پرمیوم"""
        try:
            conn = sqlite3.connect(LOCAL_DB_FILE)
            c = conn.cursor()
            c.execute('''CREATE TABLE IF NOT EXISTS content_projects (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            target_page TEXT,
                            goal TEXT,
                            created_at DATETIME DEFAULT CURRENT_TIMESTAMP)''')
            c.execute('''CREATE TABLE IF NOT EXISTS content_tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            project_id INTEGER,
                            day_index INTEGER,
                            date_fa TEXT,
                            format TEXT,
                            title TEXT,
                            scenario TEXT,
                            caption TEXT,
                            image_prompt TEXT,
                            status TEXT DEFAULT '💡 ایده‌پردازی',
                            manual_task TEXT)''')
            
            # افزودن ستون‌های جدید در صورت عدم وجود (مهاجرت دیتابیس)
            c.execute("PRAGMA table_info(content_tasks)")
            existing_cols = [col[1] for col in c.fetchall()]
            new_columns = ['reels_trend', 'story_plan', 'seo_tags']
            for col in new_columns:
                if col not in existing_cols:
                    try:
                        c.execute(f"ALTER TABLE content_tasks ADD COLUMN {col} TEXT DEFAULT ''")
                    except: pass

            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Content Factory DB Error: {e}")

    def build_ui(self):
        # ساختار گرید (سایدبار پروژه‌ها در راست، فضای کاری در چپ)
        self.grid_columnconfigure(0, weight=10) # محیط کاری (چپ)
        self.grid_columnconfigure(1, weight=3)  # لیست پروژه‌ها (راست)
        self.grid_rowconfigure(0, weight=1)

        # --- پنل مدیریت پروژه‌ها (راست) ---
        self.sidebar = ctk.CTkFrame(self, fg_color=THEME["bg_sidebar"], corner_radius=0, width=280)
        self.sidebar.grid(row=0, column=1, sticky="nsew")
        self.sidebar.pack_propagate(False)

        ctk.CTkLabel(self.sidebar, text="📂 پروژه‌های محتوایی", font=(APP_FONT, 18, "bold"), text_color=THEME["primary"]).pack(pady=(30, 10))
        
        self.btn_new_proj = ctk.CTkButton(self.sidebar, text="➕ پروژه جدید", fg_color=THEME["secondary"], font=(APP_FONT, 13, "bold"), command=self.show_new_project_form)
        self.btn_new_proj.pack(fill="x", padx=20, pady=10)
        
        self.projects_scroll = ctk.CTkScrollableFrame(self.sidebar, fg_color="transparent")
        self.projects_scroll.pack(fill="both", expand=True, padx=10, pady=10)

        # --- پنل فضای کاری اصلی (چپ) ---
        self.workspace = ctk.CTkFrame(self, fg_color="transparent")
        self.workspace.grid(row=0, column=0, sticky="nsew")

        # Header فضای کاری
        head = ctk.CTkFrame(self.workspace, fg_color="transparent")
        head.pack(fill="x", padx=30, pady=20)
        
        self.lbl_ws_title = ctk.CTkLabel(head, text="🏭 دستیار هوشمند محتوا (AI Manager)", font=(APP_FONT, 26, "bold"), text_color="white")
        self.lbl_ws_title.pack(side="right")
        self.lbl_ws_goal = ctk.CTkLabel(head, text="لطفاً یک پروژه را انتخاب کنید یا استراتژی جدید بسازید.", font=(APP_FONT, 12), text_color="gray")
        self.lbl_ws_goal.pack(side="right", padx=15)
        
        self.btn_export = ctk.CTkButton(head, text="📥 خروجی جامع اکسل", fg_color="#1D6F42", hover_color="#124A2B", font=(APP_FONT, 12, "bold"), command=self.export_to_excel)
        self.btn_export.pack(side="left")
        self.btn_export.pack_forget() # مخفی تا زمان انتخاب پروژه

        # کانتینر داینامیک
        self.dynamic_area = ctk.CTkFrame(self.workspace, fg_color="transparent")
        self.dynamic_area.pack(fill="both", expand=True, padx=20, pady=10)

        self.show_placeholder()

    def show_placeholder(self):
        for w in self.dynamic_area.winfo_children(): w.destroy()
        self.lbl_ws_title.configure(text="🏭 دستیار هوشمند محتوا")
        self.lbl_ws_goal.configure(text="لطفاً یک پروژه را انتخاب کنید یا استراتژی جدید بسازید.")
        self.btn_export.pack_forget()
        
        placeholder = ctk.CTkFrame(self.dynamic_area, fg_color="transparent")
        placeholder.pack(expand=True)
        ctk.CTkLabel(placeholder, text="🧠", font=("Emoji", 60)).pack(pady=10)
        ctk.CTkLabel(placeholder, text="هوش مصنوعی آماده طراحی تقویم، ریلزهای ترند و استوری‌بوردهای شماست...", font=(APP_FONT, 16), text_color="gray").pack()

    def load_projects(self):
        for w in self.projects_scroll.winfo_children(): w.destroy()
        try:
            conn = sqlite3.connect(LOCAL_DB_FILE)
            c = conn.cursor()
            c.execute("SELECT id, target_page FROM content_projects ORDER BY id DESC")
            self.projects = c.fetchall()
            conn.close()

            if not self.projects:
                ctk.CTkLabel(self.projects_scroll, text="پروژه‌ای یافت نشد.", text_color="gray", font=FONT_NORMAL).pack(pady=20)
                return

            for p_id, p_name in self.projects:
                btn = ctk.CTkButton(self.projects_scroll, text=f"📱 {p_name}", anchor="e", fg_color=THEME["bg_card"], hover_color=THEME["bg_hover"], text_color="white", font=(APP_FONT, 13, "bold"), height=40, command=lambda pid=p_id: self.open_project(pid))
                btn.pack(fill="x", pady=4)
        except Exception as e:
            print(f"Load Projects Error: {e}")

    def show_new_project_form(self):
        for w in self.dynamic_area.winfo_children(): w.destroy()
        self.current_project_id = None
        self.lbl_ws_title.configure(text="✨ ایجاد استراتژی و کمپین حرفه‌ای")
        self.lbl_ws_goal.configure(text="")
        self.btn_export.pack_forget()

        form = ctk.CTkFrame(self.dynamic_area, fg_color=THEME["bg_card"], corner_radius=20, border_width=1, border_color=THEME["border"])
        form.pack(pady=40, padx=40, fill="x")

        ctk.CTkLabel(form, text="آیدی پیج / نام برند (هدف):", font=(APP_FONT, 12, "bold")).pack(anchor="e", padx=30, pady=(30, 5))
        ent_target = ctk.CTkEntry(form, font=(APP_FONT, 14), justify="right", fg_color=THEME["bg_input"], height=40)
        ent_target.pack(fill="x", padx=30)
        add_context_menu(ent_target)

        ctk.CTkLabel(form, text="هدف اصلی کمپین (بسیار مهم برای هوش مصنوعی):", font=(APP_FONT, 12, "bold")).pack(anchor="e", padx=30, pady=(20, 5))
        ent_goal = ctk.CTkEntry(form, font=(APP_FONT, 14), justify="right", fg_color=THEME["bg_input"], height=40, placeholder_text="مثال: لانچ محصول جدید، افزایش آگاهی از برند، رشد فالوور، فروش ویژه...")
        ent_goal.pack(fill="x", padx=30)
        add_context_menu(ent_goal)

        btn_generate = ctk.CTkButton(form, text="🧠 تحلیل و ساخت تقویم جامع ۳۰ روزه", fg_color=THEME["primary"], hover_color=THEME["primary_hover"], height=50, font=(APP_FONT, 15, "bold"), command=lambda: self.generate_new_plan(ent_target.get(), ent_goal.get(), btn_generate))
        btn_generate.pack(fill="x", padx=30, pady=40)

    def generate_new_plan(self, target, goal, btn):
        if not target or not goal:
            messagebox.showerror("خطا", "لطفاً پیج هدف و مقصود کمپین را مشخص کنید.")
            return
        btn.configure(state="disabled", text="⏳ در حال آنالیز رقبا، یافتن ترندها و مهندسی استراتژی...")
        threading.Thread(target=self._ai_generation_worker, args=(target, goal, btn), daemon=True).start()

    def _ai_generation_worker(self, target, goal, btn):
        try:
            conn = sqlite3.connect(LOCAL_DB_FILE)
            c = conn.cursor()
            c.execute("INSERT INTO content_projects (target_page, goal) VALUES (?, ?)", (target, goal))
            p_id = c.lastrowid
            
            # دریافت محصولات از CRM برای تزریق به هوش مصنوعی
            crm_products = AIBrain._build_product_knowledge_base() if hasattr(AIBrain, '_build_product_knowledge_base') else "محصولات مشخص نشده است."

            # استفاده از الحاق رشته‌ای ایمن جهت جلوگیری از خطای پارسر پایتون 3.13 و ویرگول فارسی
            sys_msg = (
                "شما استراتژیست ارشد، ادمین حرفه‌ای شبکه‌های اجتماعی و ترندیاب هستید. "
                "وظیفه شما طراحی یک تقویم محتوایی 30 روزه، کاملاً بدون تکرار و حرفه‌ای برای برند '" 
                + str(target) + "' با هدف اصلی '" + str(goal) + "' است.\n"
                "لطفاً محصولات و خدمات زیر را به‌طور هوشمندانه در استوری‌ها و کال‌تراکشن‌ها (CTA) ادغام کنید:\n"
                + str(crm_products)
            )
            prompt = (
                "خروجی را فقط و فقط به فرمت یک آرایه JSON معتبر بدهید بدون متن اضافی.\n"
                "هر آبجکت در آرایه باید دقیقاً شامل فیلدهای زیر باشد:\n"
                '"day": شماره روز (1 تا 30)\n'
                '"format": نوع محتوا (مثل: ریلز وایرال، ریلز آموزشی، پست اسلایدی، میم ترند)\n'
                '"title": تیتر بسیار جذاب و هوک‌دار (قلاب)\n'
                '"scenario": سناریوی دقیق (شروع، بدنه، دعوت به اقدام)\n'
                '"reels_trend": پیشنهاد موزیک ترند، افکت، یا سبک ادیت برای این روز\n'
                '"story_plan": سناریوی 4 مرحله‌ای استوری برای این روز (حتماً ترکیبی از تعامل، پشت صحنه و محصولات/خدمات)\n'
                '"manual_task": یک تسک عملیاتی برای ادمین در این روز (مثلاً: آنالیز اینسایت، لایک 20 همکار)\n'
            )
            
            plan_json = []
            try:
                if AI_AVAILABLE:
                    client = G4FClient()
                    res = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": sys_msg}, {"role": "user", "content": prompt}])
                    raw = res.choices[0].message.content
                    clean_raw = raw[raw.find('['):raw.rfind(']')+1]
                    plan_json = json.loads(clean_raw)
            except Exception as ai_e:
                print(f"AI VIP Plan Error: {ai_e}")
                
            # فال‌بک تولید هوشمند در صورت خرابی یا قطع بودن AI (با ساختار کامل پرمیوم)
            if not plan_json or len(plan_json) < 5:
                plan_json = []
                for i in range(1, 31):
                    is_reels = (i % 2 != 0)
                    frmt = "ریلز ترند 🎬" if is_reels else "پست اسلایدی (آلبوم) 📸"
                    trend = "استفاده از صدای ترند (Trending Audio) + سرعت ادیت سینک با بیت" if is_reels else "بدون نیاز به موزیک ترند"
                    
                    plan_json.append({
                        "day": i, 
                        "format": frmt, 
                        "title": f"قلاب جذاب مرتبط با {goal}", 
                        "scenario": "ثانیه 1-3: هوک قوی (چرا این ویدیو رو باید ببینی؟)\nثانیه 3-12: ارزش اصلی یا آموزش\nثانیه 12-15: دعوت به اکشن (ذخیره کن، کامنت بذار)",
                        "reels_trend": trend,
                        "story_plan": f"استوری 1: نظرسنجی روزمره\nاستوری 2: ارتباط موضوع با {goal}\nاستوری 3: معرفی غیرمستقیم یکی از محصولات\nاستوری 4: لینک یا CTA",
                        "manual_task": "تعامل با 10 پیج هم‌رده + پاسخ‌دهی به دایرکت‌های صبحگاهی"
                    })

            start_date = datetime.now()
            for item in plan_json:
                day_idx = int(item.get("day", 1))
                cur_date = start_date + timedelta(days=day_idx-1)
                date_fa = jdatetime.date.fromgregorian(date=cur_date.date()).strftime("%Y/%m/%d") if JALALI_AVAILABLE else cur_date.strftime("%Y-%m-%d")
                
                c.execute("""INSERT INTO content_tasks 
                             (project_id, day_index, date_fa, format, title, scenario, caption, image_prompt, status, manual_task, reels_trend, story_plan, seo_tags) 
                             VALUES (?, ?, ?, ?, ?, ?, '', '', '💡 ایده‌پردازی', ?, ?, ?, '')""", 
                          (p_id, day_idx, date_fa, 
                           str(item.get("format", "")), str(item.get("title", "")), str(item.get("scenario", "")),
                           str(item.get("manual_task", "")), str(item.get("reels_trend", "")), str(item.get("story_plan", ""))))
            
            conn.commit()
            conn.close()

            self.after(0, lambda: [
                self.load_projects(),
                self.open_project(p_id),
                messagebox.showinfo("عملیات موفق", "تقویم محتوایی اختصاصی و ترندهای شما با موفقیت طراحی شد!")
            ])

        except Exception as e:
            self.after(0, lambda: [
                btn.configure(state="normal", text="🧠 تحلیل و ساخت تقویم جامع ۳۰ روزه"),
                messagebox.showerror("خطا", f"خطا در تولید تقویم:\n{e}")
            ])

    def open_project(self, project_id):
        self.current_project_id = project_id
        try:
            conn = sqlite3.connect(LOCAL_DB_FILE)
            conn.row_factory = sqlite3.Row
            c = conn.cursor()
            
            c.execute("SELECT * FROM content_projects WHERE id = ?", (project_id,))
            proj = c.fetchone()
            
            c.execute("SELECT * FROM content_tasks WHERE project_id = ? ORDER BY day_index ASC", (project_id,))
            tasks = [dict(row) for row in c.fetchall()]
            conn.close()
            
            self.plan_data = tasks
            self.lbl_ws_title.configure(text=f"📱 داشبورد محتوا: {proj['target_page']}")
            self.lbl_ws_goal.configure(text=f"🎯 استراتژی: {proj['goal']}")
            self.btn_export.pack(side="left")
            
            self.render_calendar_grid()
        except Exception as e:
            print(f"Open Project Error: {e}")

    def render_calendar_grid(self):
        for w in self.dynamic_area.winfo_children(): w.destroy()
        
        scroll = ctk.CTkScrollableFrame(self.dynamic_area, fg_color="transparent")
        scroll.pack(fill="both", expand=True)
        
        days_header = ctk.CTkFrame(scroll, fg_color=THEME["bg_card"], height=40, corner_radius=8)
        days_header.pack(fill="x", pady=(0, 10))
        week_days = ["روز اول", "روز دوم", "روز سوم", "روز چهارم", "روز پنجم", "روز ششم", "روز هفتم"]
        for i in range(7): days_header.grid_columnconfigure(i, weight=1)
        for i, day in enumerate(reversed(week_days)): 
            ctk.CTkLabel(days_header, text=day, font=(APP_FONT, 12, "bold"), text_color=THEME["text_dim"]).grid(row=0, column=i, pady=10)

        grid_frame = ctk.CTkFrame(scroll, fg_color="transparent")
        grid_frame.pack(fill="both", expand=True)
        for i in range(7): grid_frame.grid_columnconfigure(i, weight=1)

        row = 0; col = 6
        for task in self.plan_data:
            self._create_kanban_card(grid_frame, task, row, col)
            col -= 1
            if col < 0: col = 6; row += 1

    def _create_kanban_card(self, parent, task, r, c):
        status = task.get("status", "💡 ایده‌پردازی")
        border_color = self.STATUS_COLORS.get(status, "#333")
        
        card = ctk.CTkFrame(parent, fg_color=THEME["bg_card"], border_color=border_color, border_width=2, corner_radius=12)
        card.grid(row=r, column=c, padx=6, pady=6, sticky="nsew")
        card.grid_propagate(False); card.configure(height=170)

        head = ctk.CTkFrame(card, fg_color="transparent", height=25)
        head.pack(fill="x", padx=8, pady=(8, 0))
        ctk.CTkLabel(head, text=task['date_fa'], font=("vazir", 10, "bold"), text_color="gray").pack(side="right")
        
        # آیکون نوع محتوا
        f_icon = "🎬" if "ریلز" in str(task['format']) else ("📸" if "پست" in str(task['format']) else "📱")
        ctk.CTkLabel(head, text=f"{f_icon} {status}", font=(APP_FONT, 9, "bold"), text_color=border_color).pack(side="left")

        body = ctk.CTkFrame(card, fg_color="transparent")
        body.pack(fill="both", expand=True, padx=8, pady=5)
        
        format_str = task['format']
        title_str = task['title'] if len(task['title']) < 25 else task['title'][:25] + "..."
        
        ctk.CTkLabel(body, text=format_str, font=(APP_FONT, 10, "bold"), text_color="#FFF").pack(anchor="e")
        ctk.CTkLabel(body, text=title_str, font=(APP_FONT, 11), text_color="#CCC", justify="right", wraplength=120).pack(anchor="e", pady=(2,0))

        # دکمه ورود به کارت پرمیوم
        ctk.CTkButton(card, text="ویرایش و ابزارها ⚙️", height=26, font=(APP_FONT, 11, "bold"), fg_color=border_color, hover_color=THEME["bg_hover"], text_color="white", command=lambda: self.open_task_modal(task)).pack(side="bottom", fill="x", padx=8, pady=8)

    def open_task_modal(self, task):
        win = ctk.CTkToplevel(self)
        win.title(f"مدیریت حرفه‌ای محتوا - {task['date_fa']}")
        win.geometry("950x850")
        win.configure(fg_color=THEME["bg_root"])
        win.attributes("-topmost", True)
        
        # هدر اصلی
        h_frame = ctk.CTkFrame(win, fg_color=THEME["bg_card"], corner_radius=0)
        h_frame.pack(fill="x")
        ctk.CTkLabel(h_frame, text=f"📋 {task['title']}", font=(APP_FONT, 20, "bold"), text_color="white").pack(side="right", padx=20, pady=15)
        
        cmb_status = ctk.CTkComboBox(h_frame, values=list(self.STATUS_COLORS.keys()), font=(APP_FONT, 13, "bold"), justify="right", fg_color=THEME["bg_input"], width=180)
        cmb_status.pack(side="left", padx=20, pady=15)
        cmb_status.set(task['status'])

        # تب‌بندی بخش‌های مختلف
        tabs = ctk.CTkTabview(win, fg_color="transparent", segmented_button_selected_color=THEME["primary"], text_color="white")
        tabs.pack(fill="both", expand=True, padx=20, pady=10)
        tabs._segmented_button.configure(font=(APP_FONT, 13, "bold"))
        
        t_post = tabs.add("🎬 پست و ریلز")
        t_story = tabs.add("📱 استوری‌بورد")
        t_seo = tabs.add("🚀 سئو و کاور")
        t_tasks = tabs.add("✅ تسک‌ها و یادآور")

        # --- TAB 1: POST & REELS ---
        scroll_post = ctk.CTkScrollableFrame(t_post, fg_color="transparent")
        scroll_post.pack(fill="both", expand=True)
        
        ctk.CTkLabel(scroll_post, text="نوع محتوا:", font=(APP_FONT, 12, "bold"), text_color="gray").pack(anchor="e", pady=(5,0))
        txt_format = ctk.CTkEntry(scroll_post, font=(APP_FONT, 14), justify="right", fg_color=THEME["bg_input"])
        txt_format.pack(fill="x", pady=5); txt_format.insert(0, task['format'])

        ctk.CTkLabel(scroll_post, text="عنوان / قلاب (Hook):", font=(APP_FONT, 12, "bold"), text_color="gray").pack(anchor="e", pady=(10,0))
        txt_title = ctk.CTkEntry(scroll_post, font=(APP_FONT, 14), justify="right", fg_color=THEME["bg_input"])
        txt_title.pack(fill="x", pady=5); txt_title.insert(0, task['title'])

        ctk.CTkLabel(scroll_post, text="📝 سناریو دقیق (ثانیه به ثانیه):", font=(APP_FONT, 14, "bold"), text_color=THEME["primary"]).pack(anchor="e", pady=(15, 5))
        txt_scenario = ctk.CTkTextbox(scroll_post, height=120, font=(APP_FONT, 13), fg_color=THEME["bg_input"], border_width=1, border_color=THEME["border"])
        txt_scenario.pack(fill="x"); txt_scenario.insert("1.0", task['scenario'] or "")
        txt_scenario.tag_config("rtl", justify='right'); txt_scenario.tag_add("rtl", "1.0", "end")
        add_context_menu(txt_scenario)

        ctk.CTkLabel(scroll_post, text="🔥 پیشنهاد ترند ریلز (موزیک/ادیت):", font=(APP_FONT, 14, "bold"), text_color="#E91E63").pack(anchor="e", pady=(15, 5))
        txt_trend = ctk.CTkTextbox(scroll_post, height=80, font=(APP_FONT, 13), fg_color=THEME["bg_input"], text_color="#F48FB1", border_width=1, border_color=THEME["border"])
        txt_trend.pack(fill="x"); txt_trend.insert("1.0", task.get('reels_trend', '') or "")
        txt_trend.tag_config("rtl", justify='right'); txt_trend.tag_add("rtl", "1.0", "end")
        add_context_menu(txt_trend)

        # --- TAB 2: STORYBOARD ---
        scroll_story = ctk.CTkScrollableFrame(t_story, fg_color="transparent")
        scroll_story.pack(fill="both", expand=True)

        head_story = ctk.CTkFrame(scroll_story, fg_color="transparent")
        head_story.pack(fill="x", pady=10)
        ctk.CTkLabel(head_story, text="📱 سناریوی استوری‌های امروز:", font=(APP_FONT, 14, "bold"), text_color=THEME["info"]).pack(side="right")
        
        btn_magic_story = ctk.CTkButton(head_story, text="✨ بازنویسی با محصولات CRM", fg_color=THEME["secondary"], font=(APP_FONT, 12, "bold"))
        btn_magic_story.pack(side="left")

        txt_story = ctk.CTkTextbox(scroll_story, height=250, font=(APP_FONT, 13), fg_color=THEME["bg_input"], border_width=1, border_color=THEME["border"])
        txt_story.pack(fill="x", pady=5); txt_story.insert("1.0", task.get('story_plan', '') or "")
        txt_story.tag_config("rtl", justify='right'); txt_story.tag_add("rtl", "1.0", "end")
        add_context_menu(txt_story)
        
        # --- TAB 3: SEO & CAPTION ---
        scroll_seo = ctk.CTkScrollableFrame(t_seo, fg_color="transparent")
        scroll_seo.pack(fill="both", expand=True)

        cap_head = ctk.CTkFrame(scroll_seo, fg_color="transparent")
        cap_head.pack(fill="x", pady=5)
        ctk.CTkLabel(cap_head, text="✍️ کپشن نهایی:", font=(APP_FONT, 14, "bold"), text_color=THEME["accent"]).pack(side="right")
        btn_magic_cap = ctk.CTkButton(cap_head, text="✨ تولید کپشن متقاعدکننده", fg_color=THEME["primary"], font=(APP_FONT, 12, "bold"))
        btn_magic_cap.pack(side="left")

        txt_caption = ctk.CTkTextbox(scroll_seo, height=130, font=(APP_FONT, 13), fg_color=THEME["bg_input"], border_width=1, border_color=THEME["border"])
        txt_caption.pack(fill="x"); txt_caption.insert("1.0", task['caption'] or "")
        txt_caption.tag_config("rtl", justify='right'); txt_caption.tag_add("rtl", "1.0", "end")
        add_context_menu(txt_caption)

        seo_head = ctk.CTkFrame(scroll_seo, fg_color="transparent")
        seo_head.pack(fill="x", pady=(15, 5))
        ctk.CTkLabel(seo_head, text="🔍 هشتگ‌ها و کلمات کلیدی (SEO):", font=(APP_FONT, 14, "bold"), text_color="#FFC107").pack(side="right")
        
        txt_seo = ctk.CTkTextbox(scroll_seo, height=70, font=(APP_FONT, 12), text_color="#FFE082", fg_color=THEME["bg_input"], border_width=1, border_color=THEME["border"])
        txt_seo.pack(fill="x"); txt_seo.insert("1.0", task.get('seo_tags', '') or "")
        txt_seo.tag_config("rtl", justify='right'); txt_seo.tag_add("rtl", "1.0", "end")
        add_context_menu(txt_seo)

        img_head = ctk.CTkFrame(scroll_seo, fg_color="transparent")
        img_head.pack(fill="x", pady=(15, 5))
        ctk.CTkLabel(img_head, text="🎨 پرامپت حرفه‌ای تصویر/کاور (انگلیسی):", font=(APP_FONT, 14, "bold"), text_color="#00BCD4").pack(side="right")
        btn_magic_img = ctk.CTkButton(img_head, text="✨ تولید پرامپت Midjourney", fg_color="#0097A7", font=(APP_FONT, 12, "bold"))
        btn_magic_img.pack(side="left")

        txt_prompt = ctk.CTkTextbox(scroll_seo, height=80, font=("Consolas", 12), fg_color=THEME["bg_input"], text_color="#B2EBF2", border_width=1, border_color=THEME["border"])
        txt_prompt.pack(fill="x"); txt_prompt.insert("1.0", task['image_prompt'] or "")
        add_context_menu(txt_prompt)

        # --- TAB 4: MANUAL TASKS ---
        scroll_tasks = ctk.CTkScrollableFrame(t_tasks, fg_color="transparent")
        scroll_tasks.pack(fill="both", expand=True)
        
        ctk.CTkLabel(scroll_tasks, text="📌 برنامه‌ها و یادآورهای امروزِ ادمین:", font=(APP_FONT, 14, "bold"), text_color=THEME["success"]).pack(anchor="e", pady=10)
        ctk.CTkLabel(scroll_tasks, text="تسک‌های دستی خود را اینجا بنویسید (مثلاً پاسخ به دایرکت‌ها، لایک همکاران، ساعت انتشار)", font=(APP_FONT, 11), text_color="gray").pack(anchor="e", pady=(0,10))
        
        txt_manual = ctk.CTkTextbox(scroll_tasks, height=200, font=(APP_FONT, 14), fg_color=THEME["bg_input"], border_width=1, border_color=THEME["border"])
        txt_manual.pack(fill="x"); txt_manual.insert("1.0", task.get('manual_task', '') or "")
        txt_manual.tag_config("rtl", justify='right'); txt_manual.tag_add("rtl", "1.0", "end")
        add_context_menu(txt_manual)

        # --- AI MAGIC FUNCTIONS ---
        def generate_story():
            crm_p = AIBrain._build_product_knowledge_base() if hasattr(AIBrain, '_build_product_knowledge_base') else ""
            goal = txt_title.get()
            btn_magic_story.configure(state="disabled", text="⏳ در حال نگارش استوری‌بورد...")
            def _run():
                try:
                    if AI_AVAILABLE:
                        client = G4FClient()
                        p = "یک سناریوی 4 استوری جذاب و غیرتکراری برای امروز بنویس. هدف: '" + str(goal) + "'. حتماً یکی از این محصولات/خدمات را به صورت غیرمستقیم و حرفه‌ای در استوری‌ها پروموت کن و در آخر کال تو اکشن بده:\n" + str(crm_p)
                        res = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role":"user", "content":p}])
                        story = res.choices[0].message.content
                        self.after(0, lambda: [txt_story.delete("1.0", "end"), txt_story.insert("1.0", story, "rtl"), btn_magic_story.configure(state="normal", text="✨ بازنویسی مجدد")])
                except:
                    self.after(0, lambda: [btn_magic_story.configure(state="normal", text="✨ خطا! دوباره تست کنید")])
            threading.Thread(target=_run, daemon=True).start()

        def generate_caption():
            scen = txt_scenario.get("1.0", "end").strip()
            if not scen: messagebox.showwarning("خطا", "ابتدا سناریو را بنویسید."); return
            btn_magic_cap.configure(state="disabled", text="⏳ در حال نوشتن کپشن و سئو...")
            def _run():
                try:
                    if AI_AVAILABLE:
                        client = G4FClient()
                        p = "بر اساس این سناریو یک کپشن متقاعدکننده اینستاگرام با کال‌تواکشن (CTA) بنویس. در انتهای کپشن 15 هشتگ و کلمات کلیدی سئو شده جداگانه لیست کن.\nسناریو: '" + str(scen) + "'"
                        res = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role":"user", "content":p}])
                        full_cap = res.choices[0].message.content
                        
                        # جدا کردن هشتگ‌ها اگر امکان داشت
                        cap_part = full_cap
                        seo_part = ""
                        if "#" in full_cap:
                            parts = full_cap.split("#", 1)
                            cap_part = parts[0].strip()
                            seo_part = "#" + parts[1].strip()
                            
                        self.after(0, lambda: [
                            txt_caption.delete("1.0", "end"), txt_caption.insert("1.0", cap_part, "rtl"), 
                            txt_seo.delete("1.0", "end"), txt_seo.insert("1.0", seo_part, "rtl"),
                            btn_magic_cap.configure(state="normal", text="✨ تولید مجدد")
                        ])
                except:
                    self.after(0, lambda: [btn_magic_cap.configure(state="normal", text="✨ خطا! دوباره تست کنید")])
            threading.Thread(target=_run, daemon=True).start()

        def generate_image_prompt():
            scen = txt_scenario.get("1.0", "end").strip()
            title = txt_title.get()
            btn_magic_img.configure(state="disabled", text="⏳ در حال مهندسی پرامپت...")
            def _run():
                try:
                    if AI_AVAILABLE:
                        client = G4FClient()
                        p = "Write a highly professional, detailed Midjourney v6 image generation prompt in English for a social media cover based on this title: '" + str(title) + "' and scenario: '" + str(scen) + "'. Make it cinematic lighting, 8k resolution, modern, photorealistic. Output ONLY the english prompt."
                        res = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role":"user", "content":p}])
                        prmpt = res.choices[0].message.content
                        self.after(0, lambda: [txt_prompt.delete("1.0", "end"), txt_prompt.insert("1.0", prmpt), btn_magic_img.configure(state="normal", text="✨ تولید مجدد")])
                except:
                    self.after(0, lambda: [btn_magic_img.configure(state="normal", text="✨ خطا! دوباره تست کنید")])
            threading.Thread(target=_run, daemon=True).start()

        btn_magic_story.configure(command=generate_story)
        btn_magic_cap.configure(command=generate_caption)
        btn_magic_img.configure(command=generate_image_prompt)

        # دکمه ذخیره اصلی خارج از تب‌ها قرار دارد تا همیشه در دسترس باشد
        def save_task():
            try:
                conn = sqlite3.connect(LOCAL_DB_FILE)
                c = conn.cursor()
                c.execute("""UPDATE content_tasks SET 
                             status=?, format=?, title=?, scenario=?, reels_trend=?, 
                             story_plan=?, caption=?, seo_tags=?, image_prompt=?, manual_task=? 
                             WHERE id=?""", 
                          (cmb_status.get(), txt_format.get(), txt_title.get(), 
                           txt_scenario.get("1.0", "end").strip(), txt_trend.get("1.0", "end").strip(),
                           txt_story.get("1.0", "end").strip(), txt_caption.get("1.0", "end").strip(),
                           txt_seo.get("1.0", "end").strip(), txt_prompt.get("1.0", "end").strip(),
                           txt_manual.get("1.0", "end").strip(), task['id']))
                conn.commit()
                conn.close()
                messagebox.showinfo("موفق", "تسک با موفقیت بروزرسانی شد.")
                win.destroy()
                self.open_project(self.current_project_id) # رفرش گرید
            except Exception as e:
                messagebox.showerror("خطا", str(e))

        ctk.CTkButton(win, text="💾 ذخیره تمامی تغییرات", fg_color=THEME["success"], height=55, font=(APP_FONT, 16, "bold"), command=save_task).pack(fill="x", padx=20, pady=20)

    def export_to_excel(self):
        if not self.plan_data:
            messagebox.showinfo("خطا", "داده‌ای برای خروجی وجود ندارد.")
            return
        try:
            export_data = []
            for t in self.plan_data:
                export_data.append({
                    "روز": t.get('day_index'),
                    "تاریخ": t.get('date_fa'),
                    "وضعیت": t.get('status'),
                    "نوع محتوا": t.get('format'),
                    "عنوان / قلاب": t.get('title'),
                    "سناریو پست/ریلز": t.get('scenario'),
                    "ترند ریلز": t.get('reels_trend', ''),
                    "استوری بورد": t.get('story_plan', ''),
                    "کپشن": t.get('caption'),
                    "هشتگ و سئو": t.get('seo_tags', ''),
                    "پرامپت کاور (انگلیسی)": t.get('image_prompt'),
                    "تسک‌های ادمین": t.get('manual_task', '')
                })
            
            df = pd.DataFrame(export_data)
            path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")], initialfile=f"Content_Strategy_Plan_{self.current_project_id}.xlsx")
            if path:
                df.to_excel(path, index=False)
                messagebox.showinfo("موفق", "تقویم استراتژی محتوا به صورت جامع در اکسل ذخیره شد.")
        except Exception as e:
            messagebox.showerror("خطا در خروجی", f"خطا: {e}\nاحتمالاً ماژول openpyxl نصب نیست.")

# =================================================================
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

THEME = {
    "bg_root": "#050505", "bg_sidebar": "#0B0B0B", "bg_card": "#141414", "bg_input": "#181818",
    "primary": "#8e44ad", "primary_hover": "#27ae60", "secondary": "#27ae60",
    "success": "#27ae60", "danger": "#8e44ad", "warning": "#27ae60", "info": "#3498db",
    "text_main": "#d2dae2", "text_dim": "#d2dae2",
    "border": "#2A2A2A", "bg_hover": "#1E1E1E", "chart_bg": "#141414", 
    "table_head": "#1A1A1A", "table_row_even": "#141414", "table_row_odd": "#0F0F0F",
    "whatsapp": "#25D366", "telegram": "#29B6F6", "eitaa": "#F39C12", "bale": "#4CAF50", 
    "rubika": "#8E44AD", "instagram": "#E1306C", "soroush": "#0078D7", "sms_panel": "#FF5722",
    "torob": "#D73948"
}

# =================================================================
#                  PATH CONFIGURATION (FIXED & ROBUST)
# =================================================================
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except:
    BASE_DIR = os.getcwd()

DIRS = {
    "data": os.path.join(BASE_DIR, "Data"),
    "logs": os.path.join(BASE_DIR, "Logs"),
    "config": os.path.join(BASE_DIR, "Config"),
    "exports": os.path.join(BASE_DIR, "Exports"),
    "temp": os.path.join(BASE_DIR, "Temp"),
    "drivers": os.path.join(BASE_DIR, "drivers")
}

for d in DIRS.values():
    if not os.path.exists(d): 
        try: os.makedirs(d)
        except: pass

def resource_path(relative_path):
    try: base_path = sys._MEIPASS
    except Exception: base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

LOCAL_DB_FILE = os.path.join(DIRS["data"], "ultimate_scraper_pro.db")
LICENSE_FILE = os.path.join(DIRS["config"], "license.key")
AI_CONTEXT_FILE = os.path.join(DIRS["config"], "ai_context.json")
PRODUCT_CATALOG_FILE = os.path.join(DIRS["config"], "products.json")

# =================================================================
#                  MODULE: CLOUD SYNC MANAGER (NEW)
# =================================================================
class CloudSyncManager:
    """مدیریت ارسال و همگام‌سازی لحظه‌ای لیدهای استخراج‌شده به وب‌سایت تاجربام"""
    SERVER_URL = "http://127.0.0.1:8000"
    API_TOKEN = ""
    ENABLED = True

    @classmethod
    def set_config(cls, server_url, token, enabled=True):
        if server_url and server_url.strip():
            cls.SERVER_URL = server_url.strip().rstrip('/')
        if token and token.strip():
            cls.API_TOKEN = token.strip()
        cls.ENABLED = enabled
        DatabaseHandler.set_config("cloud_api_token", cls.API_TOKEN)
        DatabaseHandler.set_config("cloud_server_url", cls.SERVER_URL)

    @classmethod
    def load_config(cls):
        cls.API_TOKEN = DatabaseHandler.get_config("cloud_api_token") or ""
        cls.SERVER_URL = DatabaseHandler.get_config("cloud_server_url") or "http://127.0.0.1:8000"

    @classmethod
    def sync_record_async(cls, title, phone, city="سراسر کشور", source="اسکرپر ویندوز", keyword=""):
        """ارسال غیرهمگام (Async) لید استخراج‌شده به سرور"""
        if not cls.ENABLED or not cls.API_TOKEN:
            return
            
        def _send():
            try:
                endpoint = f"{cls.SERVER_URL}/api/seller/radar/sync-leads"
                payload = {
                    "api_token": cls.API_TOKEN,
                    "leads": [{
                        "title": str(title)[:200],
                        "phone": str(phone),
                        "city": str(city) or "سراسر کشور",
                        "source": f"دسکتاپ: {source}",
                        "keyword": str(keyword)
                    }]
                }
                headers = {"Content-Type": "application/json"}
                res = requests.post(endpoint, json=payload, headers=headers, timeout=6)
                if res.status_code == 200:
                    print(f"☁️ [Cloud Sync OK] {phone} synced to web dashboard.")
                else:
                    print(f"☁️ [Cloud Sync Failed] Status {res.status_code}: {res.text}")
            except Exception as e:
                print(f"☁️ [Cloud Sync Error]: {e}")

        threading.Thread(target=_send, daemon=True).start()

# =================================================================
#            LOCAL BRIDGE SERVER (Web <-> Desktop Sync)
# =================================================================
active_login_window = None # ارجاع به پنجره لاگین برای ورود خودکار زنده

class LocalBridgeHandler(http.server.BaseHTTPRequestHandler):
    """هندلر سرور محلی جهت تشخیص فعال بودن دسکتاپ و دریافت مستقیم دستورات از مرورگر"""
    def _set_cors(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        
    def do_OPTIONS(self):
        self._set_cors()
        self.end_headers()

    def do_GET(self):
        self._set_cors()
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        
        if self.path == '/ping':
            resp = {"status": "online", "app": "Tajerbam_Scraper", "version": "24.5"}
            self.wfile.write(json.dumps(resp).encode('utf-8'))
        elif self.path == '/status':
            resp = {
                "status": "online",
                "token_set": bool(CloudSyncManager.API_TOKEN),
                "server_url": CloudSyncManager.SERVER_URL
            }
            self.wfile.write(json.dumps(resp).encode('utf-8'))
        else:
            self.wfile.write(json.dumps({"status": "unknown_endpoint"}).encode('utf-8'))

    def do_POST(self):
        self._set_cors()
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.end_headers()
        
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b'{}'
        
        try:
            data = json.loads(post_data.decode('utf-8'))
        except:
            data = {}

        if self.path == '/set-token':
            token = data.get('token', '')
            server_url = data.get('server_url', 'http://127.0.0.1:8000')
            CloudSyncManager.set_config(server_url, token, True)
            print(f"🔗 [Local Bridge] Token updated automatically from web browser: {token[:10]}...")
            
            # اگر پنجره لاگین باز باشد، ورود خودکار را فوراً فعال کن
            global active_login_window
            if active_login_window and hasattr(active_login_window, "auto_login_from_web"):
                active_login_window.auto_login_from_web(token)

            self.wfile.write(json.dumps({"success": True, "message": "Token set and logged in successfully"}).encode('utf-8'))
        else:
            self.wfile.write(json.dumps({"success": False, "message": "Invalid endpoint"}).encode('utf-8'))

    def log_message(self, format, *args):
        pass

def start_local_bridge_server():
    """اجرای سرور محلی در یک ترد جداگانه"""
    port = 8765
    try:
        httpd = socketserver.TCPServer(("127.0.0.1", port), LocalBridgeHandler)
        print(f"🟢 [Local Bridge Server] Running on http://127.0.0.1:{port}")
        httpd.serve_forever()
    except Exception as e:
        print(f"⚠️ [Local Bridge Error] Port {port} might be in use: {e}")

# =================================================================
DB_CONFIG = {
    "host": "5.10.248.57", "user": "winboo_sdbbsnewindbb", "password": "+!kL_wC?YSvD?lr;",
    "database": "winboo_newindbb", "charset": "utf8mb4", "cursorclass": pymysql.cursors.DictCursor, "connect_timeout": 10
}

SMS_CONFIG = {
    "DOMAIN": "payammatni.com", "username": "rightechco", "password": "09148874622", 
    "line_options": ["80008"], "cost_per_sms": 200
}

ZARINPAL_CONFIG = {
    "MERCHANT": "63c04e41-1e73-4fa7-9f84-5f6d62868a8a", 
    "ZP_API_REQUEST": "https://api.zarinpal.com/pg/v4/payment/request.json",
    "ZP_API_VERIFY": "https://api.zarinpal.com/pg/v4/payment/verify.json",
    "ZP_API_STARTPAY": "https://www.zarinpal.com/pg/StartPay/",
    "CALLBACK_URL": "https://rightechco.com/verify_payment.php",
    "CALLBACK_PORT": 12345, 
}

# تنظیمات فونت که باعث خطا شده بود
APP_FONT = "Vazir"
FONT_HEADER = (APP_FONT, 20, "bold")
FONT_TITLE = (APP_FONT, 16, "bold")
FONT_NORMAL = (APP_FONT, 12)
FONT_SMALL = (APP_FONT, 10)
FONT_MONO = (APP_FONT, 13)  # <--- فونت بخش لاگ‌ها به وزیر (Vazir) تغییر یافت

# =================================================================
#                  UTILITY CLASSES (MISSING RESTORED)
# =================================================================
def get_hwid():
    """تولید شناسه سخت‌افزاری منحصر به فرد"""
    try: return str(uuid.getnode())
    except: return "UNKNOWN_HWID"

class LoggerManager:
    @staticmethod
    def setup():
        if not os.path.exists(DIRS["logs"]): os.makedirs(DIRS["logs"])
        log_file = os.path.join(DIRS["logs"], f"winbo_{datetime.now().strftime('%Y-%m-%d')}.log")
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s', encoding='utf-8')
    @staticmethod
    def info(msg): 
        print(f"[INFO] {msg}"); 
        try: logging.info(msg)
        except: pass
    @staticmethod
    def error(msg): 
        print(f"[ERROR] {msg}"); 
        try: logging.error(msg)
        except: pass

LoggerManager.setup()

class UserAgentManager:
    AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ]
    @classmethod
    def get_random(cls): return random.choice(cls.AGENTS)

class ScraperUtils:
    _driver_path = None 
    @staticmethod
    def _find_local_driver():
        candidates = [os.path.join(BASE_DIR, "chromedriver.exe"), os.path.join(DIRS.get("drivers", ""), "chromedriver.exe"), os.path.join(DIRS.get("data", ""), "chromedriver.exe")]
        for path in candidates:
            if os.path.exists(path): return path
        return None
        
    @staticmethod
    def get_driver(headless=False):
        for k in ['HTTP_PROXY', 'HTTPS_PROXY', 'http_proxy', 'https_proxy']:
            if k in os.environ: del os.environ[k]
            
        options = Options()
        
        if headless: options.add_argument("--headless=new")
        options.add_argument(f"user-agent={UserAgentManager.get_random()}")
        options.add_argument("--disable-blink-features=AutomationControlled") 
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--log-level=3")
        options.add_argument("--silent")
        options.page_load_strategy = 'eager' 
        profile_dir = os.path.join(DIRS["temp"], "ChromeProfile_Lite")
        if not os.path.exists(profile_dir): os.makedirs(profile_dir, exist_ok=True)
        options.add_argument(f"--user-data-dir={profile_dir}")
        local_path = ScraperUtils._find_local_driver()
        if local_path:
            try:
                service = Service(executable_path=local_path)
                if platform.system() == 'Windows': service.creationflags = subprocess.CREATE_NO_WINDOW
                driver = webdriver.Chrome(service=service, options=options)
                return driver
            except: pass
        try: return webdriver.Chrome(options=options)
        except Exception as e: 
            print(f"❌ درایور یافت نشد: {e}"); return None
            
    @staticmethod
    def to_english_digits(text): 
        if not text: return ""
        return text.translate(str.maketrans("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩", "01234567890123456789"))
    @staticmethod
    def extract_phones_aggressive(text):
        if not text: return []
        text = ScraperUtils.to_english_digits(text)
        phones = re.findall(r'09\d{9}', re.sub(r'[^0-9]', '', text))
        return list(set(phones))
    @staticmethod
    def set_clipboard(text):
        try: import pyperclip; pyperclip.copy(text); return True
        except: return False
    @staticmethod
    def smart_click(driver, element):
        try: driver.execute_script("arguments[0].click();", element)
        except: element.click()
    @staticmethod
    def normalize_url(base, link): return urljoin(base, link)
    @staticmethod
    def uniq(lst): return list(dict.fromkeys(lst))
    @staticmethod
    def human_scroll(driver):
        try: driver.execute_script("window.scrollBy(0, 400);"); time.sleep(0.5)
        except: pass
    @staticmethod
    def convert_persian_digits(text): return ScraperUtils.to_english_digits(text)
    @staticmethod
    def clean_text_for_excel(text): return re.sub(r'[\x00-\x08\x0B-\x0C\x0E-\x1F]', '', str(text)).strip() if text else "نامشخص"

class SupportManager:
    @staticmethod
    def create_table_if_not_exists():
        # دیتابیس لوکال دیگر نیاز نیست. این بخش متصل به دیتابیس سایت است.
        pass
    
    @staticmethod
    def send_ticket(subject, message):
        ctx = LicenseManager.USER_CONTEXT
        if not ctx.get('is_active') or not ctx.get('user_id'): return False, "لایسنس شما فعال نیست."
        try:
            conn = pymysql.connect(**DB_CONFIG)
            with conn.cursor() as cursor:
                # 1. ساخت تیکت جدید مستقیماً روی وبسایت
                sql_ticket = "INSERT INTO tickets (user_id, subject, department, priority, status) VALUES (%s, %s, 'technical', 'medium', 'open')"
                cursor.execute(sql_ticket, (ctx['user_id'], subject))
                ticket_id = cursor.lastrowid
                
                # 2. ثبت پیام تیکت برای ادمین سایت
                sql_msg = "INSERT INTO ticket_messages (ticket_id, user_id, message, is_admin) VALUES (%s, %s, %s, 0)"
                cursor.execute(sql_msg, (ticket_id, ctx['user_id'], message))
                conn.commit()
            conn.close()
            return True, "تیکت با موفقیت به پشتیبانی آنلاین سایت ارسال شد."
        except Exception as e:
            return False, f"خطای اتصال به سرور سایت: {e}"

    @staticmethod
    def fetch_tickets():
        ctx = LicenseManager.USER_CONTEXT
        if not ctx.get('user_id'): return []
        try:
            conn = pymysql.connect(**DB_CONFIG)
            with conn.cursor() as cursor:
                # خواندن زنده تیکت‌ها و پاسخ‌های مدیران از وبسایت
                sql = """
                    SELECT t.id, t.subject, t.status, t.updated_at as created_at, 
                           (SELECT message FROM ticket_messages WHERE ticket_id = t.id AND is_admin = 0 ORDER BY id ASC LIMIT 1) as message,
                           (SELECT message FROM ticket_messages WHERE ticket_id = t.id AND is_admin = 1 ORDER BY id DESC LIMIT 1) as admin_reply
                    FROM tickets t 
                    WHERE t.user_id = %s ORDER BY t.updated_at DESC
                """
                cursor.execute(sql, (ctx['user_id'],))
                return cursor.fetchall()
        except Exception as e:
            print(f"Online Tickets Fetch Error: {e}")
            return []

def add_context_menu(widget):
    """تابع حیاتی برای افزودن منوی کلیک راست و جلوگیری از کرش کردن صفحات"""
    try:
        menu = tk.Menu(widget, tearoff=0, font=("vazir", 10))
        menu.add_command(label="کپی (Copy)", command=lambda: widget.event_generate("<<Copy>>"))
        menu.add_command(label="پیست (Paste)", command=lambda: widget.event_generate("<<Paste>>"))
        menu.add_command(label="برش (Cut)", command=lambda: widget.event_generate("<<Cut>>"))
        def show_menu(event): menu.tk_popup(event.x_root, event.y_root)
        target = widget._entry if hasattr(widget, "_entry") else (widget._textbox if hasattr(widget, "_textbox") else widget)
        target.bind("<Button-3>", show_menu)
    except: pass

# =================================================================
#                  MODULE: AI BRAIN
# =================================================================
class AIBrain:
    DATA = {
        "business_name": "کسب‌وکار من", "category": "عمومی", "tone": "دوستانه و حرفه‌ای", 
        "bot_config": {"platform_delays": {"WhatsApp": 10}, "ai_variation_enabled": False},
        "persona": "دستیار هوشمند", "sales_goal": "افزایش فروش", "usp": "کیفیت بالا",
        "business_type": "فروشگاه", "economic_logic": "رقابتی", "target_audience": "عموم",
        "objection_handling": "توضیح مزایا", "forbidden_words": "نمی‌دانم",
        "offers": "ارسال رایگان", "contact_info": ""
    }
    PRODUCTS = []

    @classmethod
    def load(cls):
        if os.path.exists(AI_CONTEXT_FILE):
            try:
                with open(AI_CONTEXT_FILE, "r", encoding="utf-8") as f: cls.DATA.update(json.load(f))
            except: pass
        if os.path.exists(PRODUCT_CATALOG_FILE):
             try:
                with open(PRODUCT_CATALOG_FILE, "r", encoding="utf-8") as f: cls.PRODUCTS = json.load(f)
             except: pass

    @classmethod
    def save(cls, new_data=None, new_products=None):
        if new_data: cls.DATA.update(new_data)
        if new_products is not None: cls.PRODUCTS = new_products
        try:
            with open(AI_CONTEXT_FILE, "w", encoding="utf-8") as f: json.dump(cls.DATA, f, ensure_ascii=False, indent=4)
            with open(PRODUCT_CATALOG_FILE, "w", encoding="utf-8") as f: json.dump(cls.PRODUCTS, f, ensure_ascii=False, indent=4)
        except: pass

    @staticmethod
    def _build_product_knowledge_base():
        if not AIBrain.PRODUCTS: return "اطلاعات محصول خاصی تعریف نشده است. تمرکز بر خدمات کلی."
        kb = "📚 **دانش‌نامه محصولات:**\n"
        for p in AIBrain.PRODUCTS:
            kb += f"🔹 **{p.get('name')}**\n   - ویژگی‌ها: {p.get('features')}\n   - قیمت اصلی: {p.get('price_main')} | 💰 قیمت ویژه: {p.get('price_off')}\n"
        return kb

    @staticmethod
    def generate_smart_reply(user_msg, msg_context="General"):
        if not AI_AVAILABLE: return "⛔ هوش مصنوعی در دسترس نیست."
        ctx = AIBrain.DATA
        products_kb = AIBrain._build_product_knowledge_base()
        
        # جایگزینی f-string با الحاق رشته جهت جلوگیری از خطای SyntaxError در پایتون 3.13
        system_instruction = (
            "شما " + str(ctx.get('persona')) + " هستید در " + str(ctx.get('business_name')) + ".\n"
            "ماموریت شما: " + str(ctx.get('sales_goal')) + ".\nلحن: " + str(ctx.get('tone')) + ".\n"
            + str(products_kb) + "\nآفرهای فعال: " + str(ctx.get('offers')) + "\n"
        )
        user_instruction = "پیام مشتری: \"" + str(user_msg) + "\"\nکانتکست: " + str(msg_context) + "\nپاسخ کوتاه و ترغیب‌کننده بنویس."
        try:
            client = G4FClient()
            response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": system_instruction}, {"role": "user", "content": user_instruction}])
            return response.choices[0].message.content
        except Exception as e: return f"خطای هوش مصنوعی: {e}"

    @staticmethod
    def generate_marketing_text(platform="SMS"):
        if not AI_AVAILABLE: return f"فروش ویژه {AIBrain.DATA.get('business_name')} آغاز شد! تماس بگیرید."
        try:
            resp = G4FClient().chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": f"Write a short Persian ad for {AIBrain.DATA.get('business_name')}."}])
            return resp.choices[0].message.content
        except: return f"فروش ویژه {AIBrain.DATA.get('business_name')} آغاز شد!"

    @staticmethod
    def generate_content_calendar(target_url, months=1):
        ctx = AIBrain.DATA
        biz_name = ctx.get('business_name', 'کسب‌وکار شما')
        category = ctx.get('category', 'عمومی')
        usp = ctx.get('usp', 'کیفیت بالا')
        
        def run_ai_task(month_idx):
            try:
                system_instruction = f"ACT AS: Senior Social Media Strategist for '{biz_name}'. CONTEXT: {category} | USP: {usp}. TASK: Create a VIP Calendar for Month {month_idx}. OUTPUT: JSON List."
                client = G4FClient()
                response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "system", "content": system_instruction}, {"role": "user", "content": f"Generate 30-day plan. Fields: day, insta_title, insta_format, insta_scenario, insta_caption, stories, engagement_plan, manual_task."}])
                content = response.choices[0].message.content.replace("```json", "").replace("```", "").strip()
                plan = json.loads(content)
                start_date = datetime.now() + timedelta(days=(month_idx-1)*30)
                for idx, day_plan in enumerate(plan):
                    current_date_g = start_date + timedelta(days=idx)
                    day_plan['date_obj'] = current_date_g.strftime("%Y-%m-%d")
                    day_plan['date_fa'] = jdatetime.date.fromgregorian(date=current_date_g.date()).strftime("%Y/%m/%d") if JALALI_AVAILABLE else f"روز {idx+1}"
                    day_plan['month_index'] = month_idx
                    day_plan['done'] = False
                    day_plan['has_post'] = True if day_plan.get('insta_format', 'Post') != 'Story Only' else False
                return plan
            except: return None

        def generate_smart_offline_plan(month_idx):
            plan = []
            start_date = datetime.now() + timedelta(days=(month_idx-1)*30)
            for i in range(1, 31):
                current_date_g = start_date + timedelta(days=i-1)
                date_fa = jdatetime.date.fromgregorian(date=current_date_g.date()).strftime("%Y/%m/%d") if JALALI_AVAILABLE else f"روز {i}"
                has_post = (i % 2 != 0)
                day_data = {'day': i, 'month_index': month_idx, 'date_fa': date_fa, 'date_obj': current_date_g.strftime("%Y-%m-%d"), 'done': False, 'has_post': has_post, 'manual_task': ""}
                day_data['engagement_plan'] = f"تعامل با همکاران در # {category.replace(' ', '_')}"
                if has_post:
                    day_data.update({'insta_title': "پست جذاب", 'insta_format': "Reels", 'insta_scenario': f"معرفی مزیت {usp}", 'insta_caption': "کپشن...", 'stories': "۴ استوری"})
                else:
                    day_data.update({'insta_title': "استراحت", 'insta_format': "Story Only", 'insta_scenario': "-", 'insta_caption': "-", 'stories': "استوری روزمره"})
                plan.append(day_data)
            return plan

        full_plan = []
        for m in range(1, months + 1):
            month_plan = run_ai_task(m) if AI_AVAILABLE and m == 1 else None
            if not month_plan: month_plan = generate_smart_offline_plan(m)
            full_plan.extend(month_plan)
        return full_plan

# =================================================================
#                  مدیریت دیتابیس (DatabaseHandler) - نسخه نهایی
# =================================================================
class DatabaseHandler:
    @staticmethod
    def initialize():
        """
        ایجاد جداول دیتابیس در صورت عدم وجود.
        شامل جداول اسکرپرها، اکانت‌ها، لاگ پیام‌ها و کیف پول.
        """
        try:
            conn = sqlite3.connect(LOCAL_DB_FILE)
            cursor = conn.cursor()
            
            schemas = {
                "divar": """CREATE TABLE IF NOT EXISTS divar (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, province TEXT, city TEXT, district TEXT, price TEXT, phone TEXT, ad_link TEXT UNIQUE, description TEXT, website TEXT, email TEXT, address TEXT, keyword TEXT, status TEXT DEFAULT 'scraped', scraped_date DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "sheypoor": """CREATE TABLE IF NOT EXISTS sheypoor (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, province TEXT, city TEXT, district TEXT, price TEXT, phone TEXT, ad_link TEXT UNIQUE, description TEXT, website TEXT, email TEXT, address TEXT, keyword TEXT, scraped_date DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "neshan": """CREATE TABLE IF NOT EXISTS neshan (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, category TEXT, address TEXT, website TEXT, email TEXT, hours TEXT, keyword TEXT, unique_id TEXT UNIQUE, scraped_date DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "niazrooz": """CREATE TABLE IF NOT EXISTS niazrooz (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, phone TEXT, owner TEXT, email TEXT, website TEXT, address TEXT, whatsapp TEXT, keyword TEXT, ad_link TEXT UNIQUE, scraped_date DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "maps": """CREATE TABLE IF NOT EXISTS maps (id INTEGER PRIMARY KEY AUTOINCREMENT, business_name TEXT, category TEXT, address TEXT, phone TEXT, website TEXT, email TEXT, hours TEXT, keyword TEXT, unique_id TEXT UNIQUE, scraped_date DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "avval": """CREATE TABLE IF NOT EXISTS avval (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, city TEXT, category TEXT, address TEXT, phone TEXT, email TEXT, website TEXT, keyword TEXT, url TEXT UNIQUE, scraped_date DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "irantejarat": """CREATE TABLE IF NOT EXISTS irantejarat (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, phone TEXT, email TEXT, website TEXT, address TEXT, location TEXT, category TEXT, keyword TEXT, url TEXT UNIQUE, scraped_date DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "instagram": """CREATE TABLE IF NOT EXISTS instagram (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, fullname TEXT, bio TEXT, phone TEXT, email TEXT, website TEXT, followers TEXT, following TEXT, posts TEXT, category TEXT, keyword TEXT, url TEXT UNIQUE, scraped_date DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "buskool": """CREATE TABLE IF NOT EXISTS buskool (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, seller TEXT, location TEXT, price TEXT, phone TEXT, description TEXT, keyword TEXT, url TEXT UNIQUE, scraped_date DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "torob": """CREATE TABLE IF NOT EXISTS torob (id INTEGER PRIMARY KEY AUTOINCREMENT, shop_name TEXT, phone TEXT, province TEXT, city TEXT, address TEXT, website TEXT, keyword TEXT, shop_link TEXT UNIQUE, scraped_date DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "accounts": """CREATE TABLE IF NOT EXISTS accounts (id INTEGER PRIMARY KEY AUTOINCREMENT, platform TEXT, identifier TEXT, api_config TEXT, credit_score INTEGER DEFAULT 50, daily_limit_max INTEGER DEFAULT 50, sent_today INTEGER DEFAULT 0, total_sent INTEGER DEFAULT 0, warmup_days INTEGER DEFAULT 0, status TEXT DEFAULT 'active', last_active DATETIME, created_at DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "message_logs": """CREATE TABLE IF NOT EXISTS message_logs (id INTEGER PRIMARY KEY AUTOINCREMENT, account_id INTEGER, recipient TEXT, message TEXT, platform TEXT, status TEXT, intent TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "wallet_transactions": """CREATE TABLE IF NOT EXISTS wallet_transactions (id INTEGER PRIMARY KEY AUTOINCREMENT, trans_type TEXT, amount INTEGER, description TEXT, date DATETIME DEFAULT CURRENT_TIMESTAMP)""",
                "app_config": """CREATE TABLE IF NOT EXISTS app_config (key TEXT PRIMARY KEY, value TEXT)"""
            }
            
            for table_name, schema in schemas.items():
                cursor.execute(schema)
                if table_name not in ['accounts', 'message_logs', 'wallet_transactions', 'app_config']:
                    DatabaseHandler._migrate_columns(cursor, table_name)
                if table_name == 'instagram':
                    try: cursor.execute("ALTER TABLE instagram ADD COLUMN category TEXT")
                    except: pass

            conn.commit()
            conn.close()
            DatabaseHandler._init_excel_files()
            
        except Exception as e:
            logging.error(f"Database Init Error: {e}")

    @staticmethod
    def get_config(key):
        try:
            conn = DatabaseHandler.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT value FROM app_config WHERE key=?", (key,))
            res = cursor.fetchone()
            conn.close()
            return res[0] if res else None
        except: return None

    @staticmethod
    def set_config(key, value):
        try:
            conn = DatabaseHandler.get_connection()
            cursor = conn.cursor()
            cursor.execute("REPLACE INTO app_config (key, value) VALUES (?, ?)", (key, value))
            conn.commit()
            conn.close()
        except: pass

    @staticmethod
    def _migrate_columns(cursor, table_name):
        try:
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [info[1] for info in cursor.fetchall()]
            needed_cols = ['email', 'website', 'address', 'keyword']
            for col in needed_cols:
                if col not in columns:
                    try: cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {col} TEXT")
                    except: pass
        except Exception as e: pass

    @staticmethod
    def _init_excel_files():
        headers_map = {
            'divar': ['عنوان', 'تلفن', 'قیمت', 'شهر', 'آدرس', 'لینک', 'ایمیل', 'وبسایت', 'کلمه کلیدی'],
            'sheypoor': ['عنوان', 'تلفن', 'قیمت', 'شهر', 'آدرس', 'لینک', 'ایمیل', 'وبسایت', 'کلمه کلیدی'],
            'neshan': ['نام', 'تلفن', 'آدرس', 'دسته‌بندی', 'لینک', 'ایمیل', 'وبسایت', 'کلمه کلیدی'],
            'niazrooz': ['عنوان', 'تلفن', 'مالک', 'آدرس', 'لینک', 'ایمیل', 'وبسایت', 'کلمه کلیدی'],
            'maps': ['نام', 'تلفن', 'آدرس', 'دسته‌بندی', 'لینک', 'ایمیل', 'وبسایت', 'کلمه کلیدی'],
            'avval': ['عنوان', 'تلفن', 'شهر', 'فعالیت', 'آدرس', 'لینک', 'ایمیل', 'وبسایت', 'کلمه کلیدی'],
            'irantejarat': ['عنوان', 'تلفن', 'مکان', 'ایمیل', 'وبسایت', 'آدرس', 'لینک', 'کلمه کلیدی'],
            'buskool': ['عنوان', 'فروشنده', 'مکان', 'قیمت', 'تلفن', 'توضیحات', 'لینک', 'کلمه کلیدی'],
            'torob': ['نام فروشگاه', 'تلفن', 'استان', 'شهر', 'آدرس', 'وبسایت', 'لینک', 'کلمه کلیدی'] 
        }
        for name, cols in headers_map.items():
            path = os.path.join(DIRS["exports"], f"{name}_data.xlsx")
            if not os.path.exists(path):
                try: pd.DataFrame(columns=cols).to_excel(path, index=False)
                except: pass

    @staticmethod
    def get_connection():
        return sqlite3.connect(LOCAL_DB_FILE)

    # تعریف قفل برای جلوگیری از تداخل نوشتاری در اکسل و دیتابیس
    _io_lock = threading.Lock()

    @staticmethod
    def save_record(table, data):
        """
        متد تضمینی و نهایی برای ذخیره داده‌ها در CRM، اکسل و همگام‌سازی لحظه‌ای با پنل وب.
        """
        with DatabaseHandler._io_lock:
            try:
                # --- بخش ۱: آماده‌سازی و تمیزکاری داده‌ها ---
                safe_data = {}
                for k, v in data.items():
                    val = str(v).strip() if v is not None else "-"
                    val = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', val)
                    safe_data[k] = val

                if 'scraped_date' not in safe_data:
                    safe_data['scraped_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # --- بخش ۲: ذخیره در دیتابیس (CRM) ---
                conn = sqlite3.connect(LOCAL_DB_FILE)
                cursor = conn.cursor()

                try:
                    cursor.execute(f"PRAGMA table_info({table})")
                    current_cols = [c[1] for c in cursor.fetchall()]
                    for col_name in safe_data.keys():
                        if col_name not in current_cols:
                            try: 
                                cursor.execute(f"ALTER TABLE {table} ADD COLUMN {col_name} TEXT")
                            except: pass
                except: pass

                cols = list(safe_data.keys())
                placeholders = ",".join(["?"] * len(cols))
                query = f"INSERT INTO {table} ({','.join(cols)}) VALUES ({placeholders})"
                
                cursor.execute(query, list(safe_data.values()))
                conn.commit()
                conn.close()

                # --- بخش ۳: همگام‌سازی خودکار با وب‌سایت (Cloud Sync) ---
                phone_num = safe_data.get('phone') or safe_data.get('mobile') or safe_data.get('tel')
                if phone_num and phone_num != "Hidden" and len(phone_num) >= 8:
                    title = safe_data.get('title') or safe_data.get('name') or safe_data.get('shop_name') or safe_data.get('username') or "کسب‌وکار"
                    city = safe_data.get('city') or safe_data.get('province') or safe_data.get('location') or "سراسر کشور"
                    keyword = safe_data.get('keyword') or safe_data.get('category') or ""
                    
                    CloudSyncManager.sync_record_async(title=title, phone=phone_num, city=city, source=table.capitalize(), keyword=keyword)

                # --- بخش ۴: ذخیره در فایل اکسل ---
                if DATA_ANALYSIS_AVAILABLE:
                    try:
                        if not os.path.exists(DIRS["exports"]): 
                            os.makedirs(DIRS["exports"])
                        
                        file_path = os.path.join(DIRS["exports"], f"{table}_data.xlsx")
                        new_row_df = pd.DataFrame([safe_data])
                        
                        if os.path.exists(file_path):
                            existing_df = pd.read_excel(file_path)
                            combined_df = pd.concat([existing_df, new_row_df], ignore_index=True)
                            combined_df.to_excel(file_path, index=False)
                        else:
                            new_row_df.to_excel(file_path, index=False)
                            
                    except Exception as e:
                        print(f"Excel Save Error ({table}): {e}")

                try:
                    LicenseManager.USER_CONTEXT['used_records'] = LicenseManager.USER_CONTEXT.get('used_records', 0) + 1
                except: pass

                return True, "Success"

            except sqlite3.IntegrityError:
                return False, "Duplicate"
            except Exception as e:
                print(f"Critical Save Error: {e}")
                return False, str(e)

    @staticmethod
    def is_duplicate(table, url):
        try:
            conn = DatabaseHandler.get_connection()
            cursor = conn.cursor()
            link_col = "url"
            if table in ["divar", "sheypoor", "niazrooz"]: link_col = "ad_link"
            elif table == "torob": link_col = "shop_link"
            elif table == "neshan" or table == "maps": link_col = "unique_id"
            cursor.execute(f"SELECT id FROM {table} WHERE {link_col}=?", (url,))
            result = cursor.fetchone()
            conn.close()
            return result is not None
        except: return False

    @staticmethod
    def fetch_crm_data(table, keyword_filter=None):
        """
        بازخوانی هوشمند داده‌ها برای نمایش در جدول CRM
        """
        try:
            conn = sqlite3.connect(LOCAL_DB_FILE)
            conn.row_factory = sqlite3.Row  # دسترسی به ستون‌ها با نام
            cursor = conn.cursor()
            
            # ساخت کوئری پایه
            sql = f"SELECT * FROM {table}"
            params = []
            
            # اعمال فیلتر جستجو روی تمام ستون‌های متنی
            if keyword_filter:
                try:
                    cursor.execute(f"PRAGMA table_info({table})")
                    cols = [c[1] for c in cursor.fetchall()]
                    # فقط در ستون‌های متنی و مهم جستجو کن
                    search_cols = [c for c in cols if 'date' not in c and 'id' != c]
                    if search_cols:
                        conditions = [f"{col} LIKE ?" for col in search_cols]
                        sql += " WHERE " + " OR ".join(conditions)
                        params = [f"%{keyword_filter}%"] * len(conditions)
                except: pass
            
            sql += " ORDER BY id DESC LIMIT 2000" # محدودیت برای جلوگیری از هنگ کردن UI
            
            cursor.execute(sql, params)
            rows = cursor.fetchall()
            conn.close()
            
            formatted_rows = []
            for row in rows:
                r_dict = dict(row)
                
                # استخراج هوشمند فیلدها (چون نام ستون‌ها در جداول مختلف متفاوت است)
                # 1. عنوان / نام
                c1 = (r_dict.get('title') or r_dict.get('name') or r_dict.get('shop_name') or 
                      r_dict.get('business_name') or r_dict.get('username') or r_dict.get('fullname') or "-")
                
                # 2. تلفن
                c2 = (r_dict.get('phone') or r_dict.get('mobile') or r_dict.get('tel') or "-")
                
                # 3. توضیحات / آدرس
                c3 = (r_dict.get('description') or r_dict.get('address') or r_dict.get('bio') or 
                      r_dict.get('location') or r_dict.get('city') or "-")
                
                # 4. کلمه کلیدی / دسته‌بندی
                c4 = (r_dict.get('keyword') or r_dict.get('category') or "-")
                
                # فرمت خروجی استاندارد برای Treeview
                # ایندکس‌ها: 0=عنوان, 1=تلفن, 2=توضیحات, ..., 6=کلمه کلیدی
                formatted_rows.append((c1, c2, c3, "", "", "", c4))
                
            return formatted_rows
        except Exception as e:
            print(f"CRM Fetch Error: {e}")
            return []

    @staticmethod
    def fetch_phones(table):
        try:
            conn = DatabaseHandler.get_connection()
            cursor = conn.cursor()
            cursor.execute(f"SELECT phone FROM {table} WHERE phone IS NOT NULL AND phone != 'Hidden'")
            rows = cursor.fetchall()
            conn.close()
            return [r[0] for r in rows if len(r[0]) > 5]
        except: return []

    # --- WALLET METHODS (SYNCED WITH ONLINE MYSQL DB) ---
    @staticmethod
    def get_wallet_balance():
        user_id = LicenseManager.USER_CONTEXT.get('user_id')
        if not user_id: return 0
        conn = None
        try:
            conn = pymysql.connect(**DB_CONFIG)
            with conn.cursor() as cursor:
                cursor.execute("SELECT wallet_balance FROM users WHERE id = %s", (user_id,))
                res = cursor.fetchone()
                bal = res.get('wallet_balance', 0) if res else 0
                LicenseManager.USER_CONTEXT['wallet'] = bal
                return bal
        except Exception as e:
            print(f"Online Wallet Sync Error: {e}")
            return LicenseManager.USER_CONTEXT.get('wallet', 0)
        finally:
            if conn and conn.open: conn.close()

    @staticmethod
    def add_wallet_transaction(trans_type, amount, description):
        user_id = LicenseManager.USER_CONTEXT.get('user_id')
        if not user_id: return
        
        # مپ کردن نوع تراکنش برای دیتابیس آنلاین
        db_trans_type = 'charge_wallet' if trans_type == 'deposit' else 'app_usage'
        db_status = 'success'
        conn = None
        try:
            conn = pymysql.connect(**DB_CONFIG)
            with conn.cursor() as cursor:
                # 1. بروزرسانی موجودی کاربر در جدول users سایت
                if trans_type == 'deposit':
                    cursor.execute("UPDATE users SET wallet_balance = wallet_balance + %s WHERE id = %s", (amount, user_id))
                elif trans_type == 'withdraw':
                    cursor.execute("UPDATE users SET wallet_balance = wallet_balance - %s WHERE id = %s", (amount, user_id))
                
                # 2. ثبت تاریخچه تراکنش در جدول transactions سایت
                try:
                    cursor.execute("INSERT INTO transactions (user_id, amount, type, status) VALUES (%s, %s, %s, %s)", 
                                   (user_id, amount, db_trans_type, db_status))
                except: 
                    # نادیده گرفتن خطا در صورتی که ستون ENUM دیتابیس هنوز مقادیر جدید را نپذیرد
                    pass
                    
                conn.commit()
        except Exception as e:
            print(f"Online Transaction Error: {e}")
        finally:
            if conn and conn.open: conn.close()

    @staticmethod
    def get_wallet_history():
        user_id = LicenseManager.USER_CONTEXT.get('user_id')
        if not user_id: return []
        conn = None
        try:
            conn = pymysql.connect(**DB_CONFIG)
            with conn.cursor() as cursor:
                # خواندن ۵۰ تراکنش آخر کاربر از دیتابیس سایت
                cursor.execute("SELECT id, type, amount, status, created_at FROM transactions WHERE user_id = %s ORDER BY id DESC LIMIT 50", (user_id,))
                rows = cursor.fetchall()
                
                formatted_rows = []
                for r in rows:
                    # تعیین واریز یا برداشت بودن
                    t_type = "deposit" if r['type'] in ['charge_wallet', 'deposit'] else "withdraw"
                    
                    # ترجمه نوع تراکنش به فارسی برای نمایش در اپلیکیشن
                    desc_map = {
                        'charge_wallet': 'شارژ مستقیم کیف پول',
                        'buy_bot': 'خرید ماژول (از مارکت)',
                        'buy_base_plan': 'خرید یا تمدید لایسنس',
                        'app_usage': 'هزینه مصرف درون برنامه‌ای (پیامک)'
                    }
                    desc = desc_map.get(r['type'], r['type'])
                    
                    formatted_rows.append((r['id'], t_type, r['amount'], desc, str(r['created_at'])[:16]))
                return formatted_rows
        except Exception as e:
            print(f"Online History Error: {e}")
            return []
        finally:
            if conn and conn.open: conn.close()

    # --- DASHBOARD STATS ---
    @staticmethod
    def get_dashboard_stats():
        stats = {'total': 0, 'today': 0}
        tables = ["divar", "sheypoor", "neshan", "instagram", "buskool", "torob", "niazrooz", "maps", "avval", "irantejarat"]
        try:
            conn = DatabaseHandler.get_connection()
            cursor = conn.cursor()
            today_str = datetime.now().strftime("%Y-%m-%d")
            for t in tables:
                try:
                    cursor.execute(f"SELECT COUNT(*) FROM {t}")
                    count = cursor.fetchone()[0]
                    stats['total'] += count
                    stats[t] = count
                    cursor.execute(f"SELECT COUNT(*) FROM {t} WHERE scraped_date LIKE '{today_str}%'")
                    t_count = cursor.fetchone()[0]
                    stats['today'] += t_count
                except: stats[t] = 0
            conn.close()
        except Exception as e: print(f"Stats Error: {e}")
        return stats

    @staticmethod
    def get_message_logs():
        try:
            conn = DatabaseHandler.get_connection()
            cursor = conn.cursor()
            # بررسی وجود ستون‌ها برای جلوگیری از کرش در دیتابیس‌های قدیمی
            try:
                cursor.execute("SELECT recipient, message, platform, status, intent, timestamp FROM message_logs ORDER BY id DESC LIMIT 2000")
            except:
                # فال‌بک برای دیتابیس‌های آپدیت نشده
                cursor.execute("SELECT recipient, message, platform, status, 'ارسال' as intent, CURRENT_TIMESTAMP as timestamp FROM message_logs ORDER BY id DESC LIMIT 2000")
            
            rows = cursor.fetchall()
            conn.close()
            return rows
        except Exception as e: 
            print(f"Fetch Logs Error: {e}")
            return []
        
    @staticmethod
    def log_message(recipient, message, platform, status, intent):
        # استفاده از قفل Thread برای جلوگیری از خطای Database is locked هنگام ارسال انبوه
        with DatabaseHandler._io_lock:
            try:
                conn = DatabaseHandler.get_connection()
                cursor = conn.cursor()
                
                # بروزرسانی خودکار جدول در صورت استفاده از فایل دیتابیس قدیمی
                try:
                    cursor.execute("PRAGMA table_info(message_logs)")
                    existing_cols = [c[1] for c in cursor.fetchall()]
                    if 'timestamp' not in existing_cols:
                        cursor.execute("ALTER TABLE message_logs ADD COLUMN timestamp DATETIME")
                    if 'intent' not in existing_cols:
                        cursor.execute("ALTER TABLE message_logs ADD COLUMN intent TEXT")
                    if 'account_id' not in existing_cols:
                        cursor.execute("ALTER TABLE message_logs ADD COLUMN account_id INTEGER DEFAULT 0")
                except: pass

                # ثبت دقیق زمان محلی سیستم
                local_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                cursor.execute("INSERT INTO message_logs (account_id, recipient, message, platform, status, intent, timestamp) VALUES (0, ?, ?, ?, ?, ?, ?)", 
                               (str(recipient), str(message), str(platform), str(status), str(intent), local_time))
                conn.commit()
                conn.close()
                print(f"[DB LOG] Saved: {platform} -> {status} ({recipient})")
            except Exception as e: 
                print(f"[DB LOG ERROR] {e}")

    @staticmethod
    def get_daily_activity_stats(days=30):
        data = {}
        try:
            conn = DatabaseHandler.get_connection()
            cursor = conn.cursor()
            tables = ["divar", "sheypoor", "neshan", "instagram", "buskool", "torob", "niazrooz", "maps", "avval", "irantejarat"]
            
            for t in tables:
                try:
                    cursor.execute(f"SELECT substr(scraped_date, 1, 10) as day, COUNT(*) FROM {t} GROUP BY day")
                    for row in cursor.fetchall():
                        day, count = row
                        if not day: continue
                        if day not in data: data[day] = {'scraped': 0, 'sent': 0, 'scraped_details': [], 'sent_details': []}
                        data[day]['scraped'] += count
                        data[day]['scraped_details'].append(f"{t.capitalize()}: {count}")
                except: pass
                
            try:
                # تلاش برای خواندن لاگ پیام‌ها ایمن شده
                try:
                    cursor.execute("SELECT substr(timestamp, 1, 10) as day, COUNT(*) FROM message_logs GROUP BY day")
                except:
                    # اگر ستون timestamp نبود
                    cursor.execute("SELECT date('now') as day, COUNT(*) FROM message_logs GROUP BY day")
                    
                for row in cursor.fetchall():
                    day, count = row
                    if not day: continue
                    if day not in data: data[day] = {'scraped': 0, 'sent': 0, 'scraped_details': [], 'sent_details': []}
                    data[day]['sent'] += count
                    data[day]['sent_details'].append(f"پیام‌ها: {count}")
            except Exception as e:
                print(f"Daily Stats SMS Error: {e}")
                
            conn.close()
        except: pass

        # اطمینان از وجود روزهای اخیر حتی اگر خالی باشند (رفع باگ خالی ماندن نمودار)
        for i in range(days):
            d = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
            if d not in data:
                data[d] = {'scraped': 0, 'sent': 0, 'scraped_details': [], 'sent_details': []}
                
        return data

# =================================================================
#                  MODULE: DATABASE & LICENSE
# =================================================================
class LicenseManager:
    USER_CONTEXT = {
        "is_active": True,
        "user_id": 1,
        "license_key": "TAJERBAM_WEB_LICENSE",
        "customer_name": "کاربر فعال تاجربام",
        "plan": "نسخه ویژه اسکرپر تاجربام",
        "max_records": 999999,
        "used_records": 0,
        "expiry_date": "نامحدود",
        "days_left": 9999,
        "hwid": get_hwid(),
        "purchased_bots": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "wallet": 0
    }

    @classmethod
    def validate_online(cls, key, is_auto=False):
        """
        اعتبارسنجی توکن یا کد کوتاه (مانند TB-849201 یا توکن‌های طولانی وب).
        """
        current_hwid = get_hwid()
        clean_key = str(key).strip() if key else ""
        
        if clean_key and (clean_key.startswith("TB-") or len(clean_key) >= 4):
            print(f"🔑 License/Token Accepted (Tajerbam Scraper): {clean_key}")
            cls.USER_CONTEXT.update({
                "is_active": True,
                "user_id": 1,
                "license_key": clean_key,
                "customer_name": "کاربر فعال تاجربام",
                "plan": "اسکرپر تاجربام (متصل به وب)",
                "max_records": 999999,
                "expiry_date": "نامحدود",
                "days_left": 9999,
                "hwid": current_hwid,
                "max_bots": 10,
                "allowed_bots": "all",
                "wallet": 0,
                "purchased_bots": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            })
            if not is_auto:
                DatabaseHandler.set_config("license_key", clean_key)
            return True, "ورود موفقیت‌آمیز به اسکرپر تاجربام"
        
        return False, "کد کوتاه ۵-۶ رقمی یا توکن وارد شده معتبر نیست."

# =================================================================
#                  LOGIN WINDOW & GUI COMPONENTS
# =================================================================
class LoginWindow(ctk.CTkToplevel):
    def __init__(self, master_app=None):
        super().__init__(master_app)
        global active_login_window
        active_login_window = self
        
        self.master_app = master_app
        self.title("ورود به اسکرپر تاجربام - TAJERBAM SCRAPER")
        self.is_destroyed = False
        
        try:
            icon_path = resource_path(os.path.join("assest", "logo.ico"))
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)
        except: pass
        
        self.geometry("420x640") 
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.safe_destroy)
        self._center_window()
        self.build_ui()
        
        self.after(500, self.check_auto_login)

    def safe_destroy(self):
        self.is_destroyed = True
        try:
            self.quit()
            self.destroy()
        except: pass

    def auto_login_from_web(self, token):
        if self.is_destroyed: return
        print(f"⚡ [Auto Login] Automatically verifying Tajerbam token: {token}")
        self.after(0, lambda: [
            self.ent_key.delete(0, "end"),
            self.ent_key.insert(0, token),
            self.do_login()
        ])

    def paste_from_clipboard(self):
        """خواندن مستقیم کلیپ‌بورد سیستم جهت جاگذاری بی‌نقص توکن یا کد کوتاه"""
        try:
            clipboard_text = self.clipboard_get().strip()
            if clipboard_text:
                self.ent_key.delete(0, "end")
                self.ent_key.insert(0, clipboard_text)
                self.lbl_status.configure(text="✅ کد/توکن با موفقیت جاگذاری شد.", text_color=THEME["success"])
            else:
                self.lbl_status.configure(text="⚠️ حافظه کپی سیستم خالی است.", text_color=THEME["warning"])
        except Exception:
            self.lbl_status.configure(text="⚠️ عدم امکان خواندن از حافظه کپی.", text_color=THEME["warning"])

    def check_auto_login(self):
        if self.is_destroyed or not self.winfo_exists(): return
        try:
            target_key = CloudSyncManager.API_TOKEN or DatabaseHandler.get_config("license_key")
            if target_key and len(target_key) >= 4:
                self.lbl_status.configure(text="🔄 ورود خودکار به اسکرپر تاجربام...", text_color=THEME["info"])
                self.ent_key.delete(0, "end")
                self.ent_key.insert(0, target_key) 
                self.btn_login.configure(state="disabled", text="⌛ لطفاً صبر کنید...")
                threading.Thread(target=self._auto_login_process, args=(target_key,), daemon=True).start()
        except: pass

    def _center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"+{x}+{y}")

    def build_ui(self):
        self.configure(fg_color=THEME["bg_root"])
        
        logo_path = resource_path(os.path.join("assest", "logo.png"))
        logo_loaded = False
        if os.path.exists(logo_path):
            try:
                pil_img = Image.open(logo_path)
                my_image = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(120, 120))
                ctk.CTkLabel(self, text="", image=my_image).pack(pady=(25, 10))
                logo_loaded = True
            except: pass
            
        if not logo_loaded:
            ctk.CTkLabel(self, text="اسکرپر تاجربام", font=("vazir", 32, "bold"), text_color=THEME["primary"]).pack(pady=(35, 10))

        ctk.CTkLabel(self, text="TAJERBAM ENTERPRISE SCRAPER", font=("vazir", 10, "bold"), text_color="gray").pack(pady=(0, 20))

        ctk.CTkLabel(self, text="کد کوتاه (مثال: TB-849201) یا توکن وب را وارد کنید:", font=(APP_FONT, 11, "bold")).pack(pady=(0, 5))
        
        # Input Container
        input_container = ctk.CTkFrame(self, fg_color="transparent")
        input_container.pack(fill="x", padx=30, pady=5)

        self.ent_key = ctk.CTkEntry(input_container, placeholder_text="کد کوتاه (TB-XXXXXX) یا توکن", height=45, justify="center", font=("vazir", 12))
        self.ent_key.pack(fill="x", pady=(0, 8))

        # کلیدهای میانبر استاندارد Ctrl+V و Shift+Insert
        def _handle_paste_event(event):
            self.after(10, self.paste_from_clipboard)
            return "break"

        target_entry = self.ent_key._entry if hasattr(self.ent_key, "_entry") else self.ent_key
        target_entry.bind("<Control-v>", _handle_paste_event)
        target_entry.bind("<Control-V>", _handle_paste_event)
        target_entry.bind("<Shift-Insert>", _handle_paste_event)

        # منوی کلیک راست
        add_context_menu(self.ent_key)

        # Dedicated Paste Button
        self.btn_paste = ctk.CTkButton(
            input_container, 
            text="📋 جاگذاری خودکار از حافظه (Paste)", 
            height=38, 
            fg_color=THEME["bg_card"], 
            hover_color=THEME["bg_hover"], 
            text_color=THEME["info"], 
            font=(APP_FONT, 11, "bold"), 
            command=self.paste_from_clipboard
        )
        self.btn_paste.pack(fill="x")
        
        self.btn_login = ctk.CTkButton(self, text="ورود به اسکرپر تاجربام", width=300, height=45, fg_color=THEME["secondary"], font=(APP_FONT, 14, "bold"), command=self.do_login)
        self.btn_login.pack(pady=20)
        
        self.lbl_status = ctk.CTkLabel(self, text="آماده جهت اتصال به پنل وب...", text_color="gray", font=(APP_FONT, 12))
        self.lbl_status.pack(pady=5)
        
        hwid = get_hwid()
        ctk.CTkLabel(self, text=f"System HWID: {hwid}", text_color="#333", font=("vazir", 9)).pack(side="bottom", pady=10)

    def _auto_login_process(self, key):
        try:
            valid, msg = LicenseManager.validate_online(key, is_auto=True)
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(valid, msg))
        except Exception as e:
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(False, f"خطای سیستمی: {e}"))

    def do_login(self):
        key = self.ent_key.get().strip()
        if not key:
            messagebox.showerror("خطا", "لطفاً کد کوتاه (مثال: TB-849201) یا توکن را وارد کنید.")
            return

        self.btn_login.configure(state="disabled", text="⏳ در حال تایید کد...")
        self.lbl_status.configure(text="بررسی کد اتصال اسکرپر تاجربام...", text_color=THEME["info"])
        threading.Thread(target=self._login_process, args=(key,), daemon=True).start()

    def _login_process(self, key):
        try:
            valid, msg = LicenseManager.validate_online(key, is_auto=False)
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(valid, msg))
        except Exception as e:
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(False, f"خطای اتصال: {e}"))

    def _finish_login(self, valid, msg):
        if self.is_destroyed or not self.winfo_exists():
            return

        self.btn_login.configure(state="normal", text="ورود به اسکرپر تاجربام")
        
        if valid:
            self.lbl_status.configure(text="✅ ورود با موفقیت انجام شد.", text_color=THEME["success"])
            self.after(300, self._launch_main_app)
        else:
            self.lbl_status.configure(text="❌ کد نامعتبر است", text_color=THEME["danger"])
            messagebox.showerror("خطای ورود", msg)

    def _launch_main_app(self):
        if not self.is_destroyed:
            self.is_destroyed = True
            try: self.destroy() 
            except: pass
            
            if self.master_app:
                self.master_app.init_ui() 
                self.master_app.deiconify()

class PersianTextFixer:
    @staticmethod
    def fix(text):
        """حل مشکل جدا شدن حروف فارسی در نمودارها با پردازش BIDI"""
        if BIDI_AVAILABLE and text:
            try:
                reshaped_text = arabic_reshaper.reshape(str(text))
                return get_display(reshaped_text)
            except: return text
        return text
    @staticmethod
    def force_rtl(text): return text

# =================================================================
#                  MODULE 7: UNIVERSAL SOCIAL BOT (MERGED & FIXED)
# =================================================================
class BaseBotFrame(ctk.CTkFrame):
    def __init__(self, master, title_text, description, **kwargs):
        super().__init__(master, fg_color=THEME["bg_root"], **kwargs)
        self.grid_columnconfigure(0, weight=1); self.grid_columnconfigure(1, weight=0); self.grid_rowconfigure(0, weight=1)
        
        # Settings on Right (Sidebar)
        self.settings_frame = ctk.CTkFrame(self, width=320, fg_color=THEME["bg_sidebar"], corner_radius=0)
        self.settings_frame.grid(row=0, column=1, sticky="nsew")
        self.settings_frame.pack_propagate(False)
        
        # Back Button for Robots (if accessed from Hub)
        self.back_btn = ctk.CTkButton(self.settings_frame, text="🔙 بازگشت به هاب ربات‌ها", fg_color="transparent", border_width=1, command=self.go_back)
        self.back_btn.pack(pady=(10, 5), padx=20, fill="x")

        ctk.CTkLabel(self.settings_frame, text=title_text, font=FONT_HEADER, text_color=THEME["primary"]).pack(pady=(20, 10))
        ctk.CTkLabel(self.settings_frame, text=description, font=FONT_SMALL, text_color=THEME["text_dim"], wraplength=280, justify="right").pack(pady=(0, 30), padx=20)
        
        # Content on Left
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        
        # تنظیمات لاگ: فونت وزیر، راست‌چین و ظاهر مدرن
        self.log_widget = ctk.CTkTextbox(self.content_frame, font=(APP_FONT, 13), fg_color="#0F0F0F", text_color="#E0E0E0")
        self.log_widget.pack(fill="both", expand=True)
        # اعمال تگ راست‌چین (RTL) به صورت قطعی
        self.log_widget.tag_config("rtl", justify='right')
        self.log_widget.configure(state="disabled")

    def go_back(self):
        # Access the main app controller to switch back
        app = self.winfo_toplevel()
        if hasattr(app, "show_frame"):
            app.show_frame("robots_hub")

    def log(self, message, level="info"):
        self.log_widget.configure(state="normal")
        icon = "✅" if level == "success" else "❌" if level == "error" else "⚠️" if level == "warning" else "🔹"
        timestamp = datetime.now().strftime('%H:%M:%S')
        # ترکیب پیام به صورت راست‌چین استاندارد فارسی
        full_msg = f"{message} {icon} [{timestamp}]\n"
        self.log_widget.insert("end", full_msg, "rtl")
        self.log_widget.see("end")
        self.log_widget.configure(state="disabled")
        if level == "error": LoggerManager.error(message)
        else: LoggerManager.info(message)

    def add_label(self, text):
        ctk.CTkLabel(self.settings_frame, text=text, font=FONT_NORMAL, anchor="e", text_color=THEME["text_main"]).pack(fill="x", padx=20, pady=(15, 5))
    
    def add_entry(self, ph):
        e = ctk.CTkEntry(self.settings_frame, placeholder_text=ph, justify="right", font=FONT_NORMAL, height=40, fg_color=THEME["bg_input"], border_color=THEME["border"])
        e.pack(fill="x", padx=20)
        add_context_menu(e) # افزودن اتوماتیک کلیک راست
        return e
    
    def add_button(self, text, cmd, col="primary", state="normal"):
        b = ctk.CTkButton(self.settings_frame, text=text, font=(APP_FONT, 15, "bold"), fg_color=THEME.get(col, THEME["primary"]), height=45, command=cmd, state=state)
        b.pack(fill="x", padx=20, pady=10); return b
    
    def add_combobox(self, values, variable=None, command=None):
        c = ctk.CTkComboBox(self.settings_frame, values=values, variable=variable, command=command, font=FONT_NORMAL, justify="right", height=40, fg_color=THEME["bg_input"], border_color=THEME["border"], dropdown_fg_color=THEME["bg_card"])
        c.pack(fill="x", padx=20); return c
    
    def add_checkbox(self, text):
        v = ctk.BooleanVar(); c = ctk.CTkCheckBox(self.settings_frame, text=text, variable=v, font=FONT_NORMAL, hover_color=THEME["primary"])
        c.pack(fill="x", padx=20, pady=10); return c

# =================================================================
#                  MODULE 6: SCRAPER IMPLEMENTATIONS
# =================================================================

# --- سیستم هوشمند مکان‌یابی (استان‌ها و شهرهای ایران با تبدیل خودکار) ---
LOCATION_MAP = {
    "کل ایران": "iran",
    "استان تهران": "tehran-province", "استان البرز": "alborz-province", "استان اصفهان": "isfahan-province",
    "استان فارس": "fars-province", "استان خراسان رضوی": "khorasan-razavi-province", "استان آذربایجان شرقی": "east-azerbaijan-province",
    "استان مازندران": "mazandaran-province", "استان گیلان": "gilan-province", "استان خوزستان": "khuzestan-province",
    "استان قم": "qom-province", "استان آذربایجان غربی": "west-azerbaijan-province", "استان کرمان": "kerman-province",
    "استان سیستان و بلوچستان": "sistan-and-baluchestan-province", "استان یزد": "yazd-province", "استان مرکزی": "markazi-province",
    "استان هرمزگان": "hormozgan-province", "استان بوشهر": "bushehr-province", "استان قزوین": "qazvin-province",
    "استان زنجان": "zanjan-province", "استان لرستان": "lorestan-province", "استان همدان": "hamedan-province",
    "استان گلستان": "golestan-province", "استان کردستان": "kurdistan-province", "استان کرمانشاه": "kermanshah-province",
    "استان سمنان": "semnan-province", "استان اردبیل": "ardabil-province", "استان ایلام": "ilam-province",
    "استان خراسان شمالی": "north-khorasan-province", "استان خراسان جنوبی": "south-khorasan-province", "استان چهارمحال و بختیاری": "chaharmahal-and-bakhtiari-province",
    "استان کهگیلویه و بویراحمد": "kohgiluyeh-and-boyer-ahmad-province",
    "تهران": "tehran", "مشهد": "mashhad", "اصفهان": "isfahan", "کرج": "karaj", "شیراز": "shiraz",
    "تبریز": "tabriz", "قم": "qom", "اهواز": "ahvaz", "کرمانشاه": "kermanshah", "ارومیه": "urmia",
    "رشت": "rasht", "زاهدان": "zahedan", "همدان": "hamedan", "کرمان": "kerman", "یزد": "yazd",
    "اردبیل": "ardabil", "بندرعباس": "bandar-abbas", "اراک": "arak", "اسلام‌شهر": "eslamshahr", "قزوین": "qazvin",
    "زنجان": "zanjan", "خرم‌آباد": "khorramabad", "سنندج": "sanandaj", "گرگان": "gorgan", "ساری": "sari",
    "ملارد": "malard", "قدس": "qods", "کاشان": "kashan", "گلستان": "golestan", "شهریار": "shahriar",
    "دزفول": "dezful", "خمینی‌شهر": "khomeinishahr", "بروجرد": "borujerd", "نیشابور": "neyshabur", "سبزوار": "sabzevar",
    "نجف‌آباد": "najafabad", "آمل": "amol", "بابل": "babol", "ورامین": "varamin", "آبادان": "abadan",
    "پاکدشت": "pakdasht", "خوی": "khoy", "ساوه": "saveh", "بجنورد": "bojnurd", "قائم‌شهر": "qaem-shahr",
    "بوشهر": "bushehr", "قرچک": "qarchak", "سیرجان": "sirjan", "بیرجند": "birjand", "ایلام": "ilam",
    "شهرکرد": "shahr-e-kord", "سمنان": "semnan", "یاسوج": "yasuj", "کیش": "kish", "قشم": "qeshm"
}

def get_city_slug(user_input):
    """الگوریتم تبدیل هوشمند نام شهر/استان به اسلاگ فینگلیش استاندارد URL"""
    if not user_input: return "iran"
    
    # یکسان‌سازی حروف (ی و ک) و حذف فاصله‌های اضافی
    clean_input = user_input.strip().replace('ي', 'ی').replace('ك', 'ک').replace('ى', 'ی').replace('آ', 'ا')
    
    # حذف پیشوندهای اضافی برای مچ شدن بهتر با دیکشنری (مثلا اگر کاربر بنویسد "شهر تبریز")
    clean_input = clean_input.replace("شهر ", "").replace("استان ", "").replace(" شهرستان", "").strip()
    
    # 1. جستجو در دیتابیس دقیق شهرها
    if clean_input in LOCATION_MAP:
        return LOCATION_MAP[clean_input]
        
    # بررسی تطابق با نام‌های انگلیسی دیتابیس (برای اطمینان)
    for fa_name, en_slug in LOCATION_MAP.items():
        if clean_input.lower() == en_slug.lower():
            return en_slug
    
    # 2. بررسی اینکه آیا کاربر از قبل انگلیسی (فینگلیش) نوشته است؟
    if re.match(r'^[a-zA-Z0-9\-]+$', user_input):
        return user_input.lower()
    
    # 3. فال‌بک: تبدیل کاراکتر به کاراکتر برای شهرهای ناشناخته
    # اصلاح حرف ی به i برای تلفظ صحیح‌تر در URL
    charmap = {
        'ا': 'a', 'آ': 'a', 'ب': 'b', 'پ': 'p', 'ت': 't', 'ث': 's', 'ج': 'j', 'چ': 'ch', 'ح': 'h', 'خ': 'kh',
        'د': 'd', 'ذ': 'z', 'ر': 'r', 'ز': 'z', 'ژ': 'zh', 'س': 's', 'ش': 'sh', 'ص': 's', 'ض': 'z', 'ط': 't',
        'ظ': 'z', 'ع': 'a', 'غ': 'gh', 'ف': 'f', 'ق': 'q', 'ک': 'k', 'ك': 'k', 'گ': 'g', 'ل': 'l', 'م': 'm', 'ن': 'n',
        'و': 'v', 'ه': 'h', 'ی': 'i', 'ي': 'i', 'ئ': 'i', 'ى': 'i', ' ': '-', '‌': '-'
    }
    res = ""
    for char in clean_input:
        res += charmap.get(char, char)
        
    # پاکسازی کاراکترهای نامعتبر و خط تیره‌های تکراری
    res = re.sub(r'[^a-z0-9\-]', '', res)
    res = re.sub(r'\-+', '-', res).strip('-')
    
    return res if res else "iran"

# --- NEW TOROB CLASS ---
class TorobUltimateFrame(BaseBotFrame):
    def __init__(self, master):
        super().__init__(master, "ربات ترب (Torob Pro)", "استخراج لیست فروشگاه‌ها، شماره تماس و آدرس از موتور جستجوی ترب.")
        self.stop_flag = False
        self.driver = None
        self.setup_ui()

    def setup_ui(self):
        self.add_label("کلمه کلیدی (مثال: موبایل):")
        self.ent_kw = self.add_entry("موبایل")
        
        self.add_label("تعداد فروشگاه:")
        self.ent_count = self.add_entry("50")
        
        self.btn_start = self.add_button("🚀 شروع استخراج", self.start, "primary")
        self.add_button("توقف عملیات", self.stop, "danger")

    def start(self):
        kw = self.ent_kw.get().strip()
        if not kw:
            messagebox.showerror("خطا", "لطفاً کلمه کلیدی را وارد کنید.")
            return
        try: limit = int(self.ent_count.get())
        except: limit = 50
        
        self.stop_flag = False
        self.btn_start.configure(state="disabled")
        threading.Thread(target=self._run, args=(kw, limit)).start()

    def stop(self):
        self.stop_flag = True
        self.log("🛑 توقف عملیات ترب.", "error")

    def _run(self, keyword, limit):
        self.log(f"شروع استخراج از ترب برای: {keyword}", "info")
        
        if self.driver: 
            try: self.driver.quit()
            except: pass
            
        self.driver = ScraperUtils.get_driver()
        if not self.driver:
            self.btn_start.configure(state="normal")
            return
            
        try:
            # گام ۱: ورود به صفحه لیست اصلی فروشگاه‌ها
            target_url = "https://torob.com/shop-list"
            self.log(f"گام ۱: ورود به {target_url}...", "info")
            
            try:
                self.driver.set_page_load_timeout(40)
                self.driver.get(target_url)
            except Exception:
                self.log("⚠️ لود صفحه طول کشید (ادامه عملیات...)", "warning")
                try: self.driver.execute_script("window.stop();")
                except: pass
            
            time.sleep(5) # انتظار برای لود کامل UI

            # گام ۲: جستجو در باکس مخصوص (طبق درخواست کاربر)
            self.log(f"گام ۲: جستجو برای '{keyword}'...", "info")
            try:
                wait = WebDriverWait(self.driver, 20)
                # استفاده از کلاس دقیق ارائه شده توسط کاربر
                search_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.styles_searchInput__NtcLo")))
                
                search_box.click()
                time.sleep(0.5)
                # پاکسازی ورودی قبلی
                search_box.send_keys(Keys.CONTROL + "a")
                search_box.send_keys(Keys.DELETE)
                
                # تایپ کلمه کلیدی و اینتر
                search_box.send_keys(keyword)
                time.sleep(1)
                search_box.send_keys(Keys.ENTER)
                
                self.log("✅ کلمه کلیدی ارسال شد. در حال بارگذاری نتایج...", "success")
                time.sleep(8) # زمان کافی برای لود ایجکس نتایج
                
            except Exception as e:
                self.log(f"⚠️ خطا در باکس جستجو: {e}", "warning")
                self.log("🔄 تلاش با لینک مستقیم (Fallback)...", "info")
                # فال‌بک: اگر به هر دلیلی باکس پیدا نشد، از لینک مستقیم استفاده می‌کنیم تا عملیات متوقف نشود
                direct_url = f"https://torob.com/shop-list/?q={urllib.parse.quote(keyword)}"
                self.driver.get(direct_url)
                time.sleep(6)
            
            collected_links = set()
            scroll_attempts = 0
            
            # --- PHASE 1: Collect Shop Links ---
            self.log("📋 فاز ۱: جمع‌آوری لینک فروشگاه‌ها...", "info")
            while len(collected_links) < limit and not self.stop_flag:
                try:
                    # Find shop cards based on user provided structure
                    cards = self.driver.find_elements(By.CSS_SELECTOR, "a[data-testid='shop-list-item']")
                    
                    new_found = False
                    for card in cards:
                        try:
                            href = card.get_attribute("href")
                            full_url = ScraperUtils.normalize_url("https://torob.com", href)
                            
                            if full_url and full_url not in collected_links:
                                # Check duplicate in DB before adding
                                if not DatabaseHandler.is_duplicate("torob", full_url):
                                    collected_links.add(full_url)
                                    new_found = True
                        except: pass
                        
                    self.log(f"🔗 لینک‌های جمع‌شده: {len(collected_links)}", "info")
                    
                    if len(collected_links) >= limit: break
                    
                    # Scroll logic
                    ScraperUtils.human_scroll(self.driver)
                    time.sleep(2)
                    
                    if not new_found:
                        scroll_attempts += 1
                        if scroll_attempts > 5:
                            self.log("⚠️ انتهای لیست یا عدم بارگذاری بیشتر.", "warning")
                            break
                    else:
                        scroll_attempts = 0
                        
                except Exception as e:
                    self.log(f"خطا در اسکرول: {e}", "warning")
                    break

            # --- PHASE 2: Extract Details ---
            self.log(f"⛏️ فاز ۲: استخراج اطلاعات از {len(collected_links)} فروشگاه...", "info")
            
            links_list = list(collected_links)[:limit]
            
            for index, shop_url in enumerate(links_list):
                if self.stop_flag: break
                
                self.log(f"[{index+1}/{len(links_list)}] بررسی فروشگاه...", "info")
                
                try:
                    self.process_shop(shop_url, keyword) # Pass keyword
                except Exception as e:
                    self.log(f"❌ خطا در پردازش لینک: {e}", "error")
                    
                time.sleep(random.uniform(2, 4))
                
        except Exception as e:
            self.log(f"❌ خطای کلی: {e}", "error")
        finally:
            self.log("✅ پایان عملیات ترب.", "success")
            self.btn_start.configure(state="normal")
            if self.driver:
                self.driver.quit()

    def process_shop(self, url, keyword=""):
        try:
            self.driver.set_page_load_timeout(30)
            self.driver.get(url)
        except Exception:
            self.log("⚠️ لود طولانی (گذر از لود کامل)...", "warning")
            try: self.driver.execute_script("window.stop();")
            except: pass

        # Wait for potential content
        try:
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except: pass
        
        shop_name = "نامشخص"
        phone = "Hidden"
        address = "نامشخص"
        province = "نامشخص"
        city = "نامشخص"
        website = "نامشخص"
        
        # 1. Shop Name
        try:
            h1 = self.driver.find_elements(By.TAG_NAME, "h1")
            if h1: shop_name = h1[0].text.strip()
            else: shop_name = self.driver.title.split("|")[0].strip()
        except: pass

        # 2. Extract Phone
        try:
            tel_links = self.driver.find_elements(By.CSS_SELECTOR, "a[href^='tel:']")
            if tel_links:
                raw_phone = tel_links[0].get_attribute("href").replace("tel:", "").strip()
                cleaned = ScraperUtils.to_english_digits(raw_phone)
                phones = ScraperUtils.extract_phones_aggressive(cleaned)
                if phones: phone = " | ".join(phones)
            
            # Fallback if specific tag not found
            if phone == "Hidden":
                body_txt = self.driver.find_element(By.TAG_NAME, "body").text
                phones = ScraperUtils.extract_phones_aggressive(body_txt)
                if phones: phone = " | ".join(phones)
        except: pass

        # 3. Extract Address
        try:
            addr_el = self.driver.find_elements(By.TAG_NAME, "address")
            if addr_el:
                addr_text = addr_el[0].text.strip()
                try:
                    p_text = addr_el[0].find_element(By.TAG_NAME, "p").text.strip()
                    if p_text: addr_text = p_text
                except: pass

                address = addr_text.replace("آدرس:", "").strip()
                
                # Parse Province/City
                try:
                    parts = address.replace("،", " ").replace("-", " ").split()
                    if "استان:" in address:
                        province = re.search(r'استان[:\s]+([^،\n]+)', address).group(1).strip()
                    if "شهر:" in address:
                        city = re.search(r'شهر[:\s]+([^،\n]+)', address).group(1).strip()
                except: pass
        except: pass
        
        # 4. Extract Website
        try:
             links = self.driver.find_elements(By.XPATH, "//a[contains(@href, 'http') and not(contains(@href, 'torob.com'))]")
             for l in links:
                 h = l.get_attribute("href")
                 if h and "instagram" not in h and "t.me" not in h and "tel:" not in h:
                     website = h
                     break
        except: pass

        # FIX: Save even if phone is missing (but CRM will filter it out)
        if shop_name != "نامشخص":
            record = {
                "shop_name": shop_name,
                "phone": phone,
                "province": province,
                "city": city,
                "address": address,
                "website": website,
                "shop_link": url,
                "keyword": keyword # Added keyword
            }
            
            success, msg = DatabaseHandler.save_record("torob", record)
            if success:
                if phone != "Hidden":
                    self.log(f"💾 ذخیره کامل: {shop_name}", "success")
                else:
                    self.log(f"💾 ذخیره شد (بدون موبایل): {shop_name}", "info")
            else:
                self.log(f"⚠️ {msg}", "warning")
        else:
            self.log("⏭️ دیتای نامعتبر (رد شد).", "warning")

# --- END TOROB CLASS ---

class BuskoolUltimateFrame(BaseBotFrame):
    def __init__(self, master):
        super().__init__(master, "ربات باسکول", "استخراج آگهی‌های محصولات کشاورزی و عمده از سایت باسکول.")
        self.stop_flag = False
        self.driver = None
        self.setup_ui()

    def setup_ui(self):
        self.add_label("کلمه کلیدی (مثال: برنج):")
        self.ent_kw = self.add_entry("برنج")
        self.add_label("تعداد بررسی:")
        self.ent_count = self.add_entry("50")
        
        self.add_button("۱. ورود به حساب (الزامی)", self.login, "secondary")
        self.btn_start = self.add_button("۲. شروع استخراج", self.start, "primary")
        
        self.add_button("توقف عملیات", self.stop, "danger")

    def login(self):
        threading.Thread(target=self._login_t).start()

    def _login_t(self):
        self.log("🌐 در حال باز کردن صفحه ورود...", "info")
        if self.driver:
            try: self.driver.quit()
            except: pass
        self.driver = ScraperUtils.get_driver(headless=False)
        if not self.driver: return
        
        try:
            self.driver.get("https://www.buskool.com/login")
            self.log("⚠️ نکته: اگر خطای 429 دریافت کردید، دقایقی صبر کنید.", "warning")
            self.log("لطفاً وارد حساب کاربری شوید و سپس دکمه شروع را بزنید.", "info")
        except Exception as e:
            self.log(f"خطا در باز کردن صفحه: {e}", "error")
            
        self.btn_start.configure(state="normal")

    def start(self):
        kw = self.ent_kw.get().strip()
        if not kw: 
            messagebox.showerror("خطا", "لطفاً کلمه کلیدی را وارد کنید.")
            return
        try: limit = int(self.ent_count.get())
        except: limit = 50
        self.stop_flag = False
        self.btn_start.configure(state="disabled")
        threading.Thread(target=self._run, args=(kw, limit)).start()

    def stop(self):
        self.stop_flag = True
        self.log("🛑 توقف عملیات.", "error")

    def _run(self, keyword, limit):
        if not self.driver:
            self.driver = ScraperUtils.get_driver()
        
        if not self.driver: 
            self.btn_start.configure(state="normal")
            return
        
        # FIX: Clean URL without markdown
        base_url = f"https://www.buskool.com/product-list?s={urllib.parse.quote(keyword)}"
        self.log(f"هدف: {base_url}", "info")
        
        try:
            self.driver.get(base_url)
            time.sleep(5)
            
            processed_count = 0
            
            while processed_count < limit and not self.stop_flag:
                try:
                    # 1. پیدا کردن کارت‌های محصول
                    cards = self.driver.find_elements(By.CSS_SELECTOR, ".product-row-wrapper")
                    
                    # 2. اسکرول برای لود بیشتر اگر نیاز است
                    if processed_count >= len(cards):
                        self.log("🔄 در حال اسکرول...", "info")
                        ScraperUtils.human_scroll(self.driver)
                        time.sleep(4)
                        cards = self.driver.find_elements(By.CSS_SELECTOR, ".product-row-wrapper")
                        
                        if processed_count >= len(cards):
                            self.log("✅ به انتهای لیست رسیدیم.", "success")
                            break
                    
                    # 3. انتخاب کارت جاری
                    target_card = cards[processed_count]
                    
                    # اسکرول به سمت کارت
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", target_card)
                    time.sleep(1)
                    
                    # 4. باز کردن در تب جدید (روش ترکیبی)
                    original_window = self.driver.current_window_handle
                    windows_before = self.driver.window_handles
                    
                    try:
                        # تلاش برای کلیک کنترل‌شده (Ctrl+Click)
                        click_area = target_card.find_element(By.CSS_SELECTOR, ".product-top-contents")
                        ActionChains(self.driver).key_down(Keys.CONTROL).click(click_area).key_up(Keys.CONTROL).perform()
                    except:
                        try:
                            # فال‌بک: کلیک روی کل کارت
                            ActionChains(self.driver).key_down(Keys.CONTROL).click(target_card).key_up(Keys.CONTROL).perform()
                        except:
                            pass
                    
                    time.sleep(3) # صبر برای باز شدن تب
                    
                    windows_after = self.driver.window_handles
                    
                    if len(windows_after) > len(windows_before):
                        # --- حالت ۱: تب جدید باز شد ---
                        self.driver.switch_to.window(windows_after[-1])
                        self.log(f"بررسی محصول {processed_count + 1}...", "info")
                        
                        self.process_product(keyword) # Pass keyword
                        
                        # بستن تب و بازگشت
                        self.driver.close()
                        self.driver.switch_to.window(original_window)
                        
                    else:
                        # --- حالت ۲: باز شدن در همان تب (SPA) ---
                        # اگر تب جدید باز نشد، کلیک معمولی می‌کنیم و سپس برمی‌گردیم
                        self.log(f"بررسی محصول {processed_count + 1} (SPA)...", "info")
                        
                        try: target_card.click()
                        except: self.driver.execute_script("arguments[0].click();", target_card)
                        
                        time.sleep(3) 
                        
                        if "/product/" in self.driver.current_url or len(self.driver.find_elements(By.TAG_NAME, "h1")) > 0:
                            self.process_product(keyword) # Pass keyword
                            self.driver.back()
                            # انتظار برای لود مجدد لیست
                            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-row-wrapper")))
                            time.sleep(2)
                        else:
                            self.log("⚠️ عدم موفقیت در ورود به صفحه محصول.", "warning")

                    processed_count += 1
                    time.sleep(1)
                    
                except Exception as e:
                    self.log(f"⚠️ خطای حلقه: {e}", "error")
                    # ریکاوری
                    try:
                        if len(self.driver.window_handles) > 1:
                            self.driver.close()
                            self.driver.switch_to.window(self.driver.window_handles[0])
                        elif "/product/" in self.driver.current_url:
                            self.driver.back()
                    except: pass
                    processed_count += 1

        except Exception as e:
            self.log(f"❌ خطای کلی: {e}", "error")
        finally:
            self.log(f"✅ پایان عملیات. {processed_count} مورد بررسی شد.", "success")
            self.btn_start.configure(state="normal")

    def process_product(self, keyword=""):
        try:
            # 1. انتظار برای لود صفحه
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "h1"))
                )
            except:
                self.log("⚠️ لود صفحه محصول کند است.", "warning")

            url = self.driver.current_url
            title = "نامشخص"; price = "توافقی"; seller = "نامشخص"; location = "نامشخص"; phone = "Hidden"; desc = ""
            
            # --- 1. تایتل ---
            try: 
                title_el = self.driver.find_element(By.TAG_NAME, "h1")
                title = title_el.text.strip().replace("\n", " ")
            except: pass
            
            # --- 2. فروشنده و آدرس ---
            try:
                # نام فروشنده
                seller_el = self.driver.find_element(By.XPATH, "//li[.//span[contains(text(), 'نام فروشنده')]]/span[not(contains(@class, 'gray-text'))]")
                seller = seller_el.text.strip()
            except: pass
            
            try:
                # آدرس
                addr_el = self.driver.find_element(By.XPATH, "//li[.//span[contains(text(), 'آدرس')]]/span[not(contains(@class, 'gray-text'))]")
                location = addr_el.text.strip()
            except: pass

            # --- 3. قیمت ---
            try:
                price_el = self.driver.find_element(By.CSS_SELECTOR, ".price-content .price")
                price = price_el.text.strip()
            except: pass

            # --- 4. کلیک تضمینی روی دکمه تماس ---
            try:
                wait = WebDriverWait(self.driver, 5)
                
                # پیدا کردن دکمه با متن "شماره تماس" (دقیق‌ترین روش)
                # XPath: دکمه‌ای که داخلش متن 'شماره تماس' وجود دارد
                contact_btn = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(., 'شماره تماس')]")
                ))
                
                # اسکرول به دکمه
                self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", contact_btn)
                time.sleep(1)
                
                # تلاش چندگانه برای کلیک (Multi-Try Click)
                clicked = False
                try:
                    # روش 1: JS Click (معمولاً بهترین جواب را می‌دهد)
                    self.driver.execute_script("arguments[0].click();", contact_btn)
                    clicked = True
                    self.log("📞 دکمه تماس کلیک شد (JS)...", "info")
                except:
                    try:
                        # روش 2: ActionChains
                        ActionChains(self.driver).move_to_element(contact_btn).pause(0.2).click().perform()
                        clicked = True
                        self.log("📞 دکمه تماس کلیک شد (Action)...", "info")
                    except: pass
                
                if clicked:
                    # --- وقفه 3 ثانیه برای لود شماره ---
                    time.sleep(3)
                
                # استخراج شماره (از تمام منابع ممکن)
                phones_found = []
                
                # الف) بررسی لینک tel (اگر دکمه تبدیل به لینک شد)
                try:
                    links = self.driver.find_elements(By.CSS_SELECTOR, "a[href^='tel:']")
                    for l in links: 
                        phones_found.append(l.get_attribute("href").replace("tel:", "").strip())
                except: pass
                
                # ب) بررسی متن در کلاس phone-number
                try:
                    p_els = self.driver.find_elements(By.CLASS_NAME, "phone-number")
                    for p in p_els: 
                        phones_found.append(p.text.strip())
                        try: phones_found.append(p.find_element(By.TAG_NAME, "p").text.strip())
                        except: pass
                except: pass

                # ج) بررسی کل متن صفحه (Ultimate Fallback)
                # اگر هیچکدام کار نکرد، یعنی شماره در صفحه ظاهر شده ولی سلکتور ما اشتباه است
                if not phones_found:
                    body_txt = self.driver.find_element(By.TAG_NAME, "body").text
                    # جستجوی تمام الگوهای شماره موبایل در متن
                    phones_found = ScraperUtils.extract_phones_aggressive(body_txt)

                # انتخاب شماره نهایی
                for raw in phones_found:
                    clean = ScraperUtils.to_english_digits(raw)
                    clean = re.sub(r"[^0-9]", "", clean)
                    # تبدیل +98
                    if clean.startswith("98"): clean = "0" + clean[2:]
                    
                    if len(clean) >= 10 and clean.startswith("0"):
                        phone = clean
                        break
                        
            except Exception as e:
                # ممکن است دکمه وجود نداشته باشد
                # self.log(f"Contact Button Issue: {e}", "warning")
                pass

            # --- 5. توضیحات ---
            try:
                desc_el = self.driver.find_element(By.XPATH, "//div[contains(@class, 'product-description')]")
                desc = desc_el.text.strip()
            except: pass

            # ذخیره
            if phone != "Hidden" and len(phone) >= 10:
                 record = {
                     "title": title,
                     "seller": seller,
                     "location": location,
                     "price": price,
                     "phone": phone,
                     "description": desc,
                     "url": url,
                     "keyword": keyword # Added keyword
                 }
                 success, msg = DatabaseHandler.save_record("buskool", record)
                 if success: self.log(f"💾 ذخیره شد: {phone} - {seller}", "success")
                 else: self.log(f"⚠️ {msg}: {phone}", "warning")
            else:
                 self.log(f"⏭️ شماره یافت نشد (نیاز به لاگین).", "info")

        except Exception as e:
            self.log(f"⚠️ خطا در استخراج: {e}", "warning")

class InstagramUltimateFrame(BaseBotFrame):
    def __init__(self, master):
        super().__init__(master, "ربات اینستاگرام (Matrix V21 - Deep Core)", "نسخه نهایی و تضمینی: استخراج خشن از سورس گوگل و دیتای مخفی اینستاگرام.")
        self.stop_flag = False
        self.driver = None
        self.setup_ui()

    def setup_ui(self):
        self.add_label("کلمه کلیدی (مثال: سالن زیبایی):")
        self.ent_kw = self.add_entry("سالن زیبایی تهران")
        
        self.add_label("شهر (اختیاری - جهت دقت بیشتر):")
        self.ent_city = self.add_entry("تهران")
        
        self.add_label("تعداد شماره درخواستی:")
        self.ent_pages = self.add_entry("50")
        self.ent_pages.insert(0, "50")

        self.btn_start = self.add_button("🚀 شروع شکار تضمینی", self.start_extraction, "primary")
        self.add_button("🛑 توقف اضطراری", self.stop_extraction, "danger")
        
        self.log("💎 موتور V21: الگوریتم 'جاروبرقی' فعال شد. تمام اعداد مخفی در سورس استخراج می‌شوند.", "info")

    def stop_extraction(self):
        self.stop_flag = True
        self.log("⚠️ توقف توسط کاربر.", "warning")

    def start_extraction(self):
        kw = self.ent_kw.get().strip()
        city = self.ent_city.get().strip()
        try:
            limit = int(self.ent_pages.get())
        except:
            limit = 50

        if not kw:
            messagebox.showerror("خطا", "لطفاً کلمه کلیدی را وارد کنید.")
            return

        self.stop_flag = False
        self.btn_start.configure(state="disabled")
        threading.Thread(target=self._run_deep_core_engine, args=(kw, city, limit), daemon=True).start()

    def _apply_stealth(self):
        try:
            self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
                    window.chrome = { runtime: {} };
                """
            })
        except: pass

    def _normalize_text(self, text):
        """تبدیل تمام اعداد فارسی و عربی به انگلیسی"""
        if not text: return ""
        replacements = {
            '۰': '0', '۱': '1', '۲': '2', '۳': '3', '۴': '4', '۵': '5', '۶': '6', '۷': '7', '۸': '8', '۹': '9',
            '٠': '0', '١': '1', '٢': '2', '٣': '3', '٤': '4', '٥': '5', '٦': '6', '٧': '7', '٨': '8', '٩': '9'
        }
        for k, v in replacements.items():
            text = text.replace(k, v)
        return text

    def _vacuum_phones(self, text):
        """
        الگوریتم جاروبرقی:
        حذف تمام کاراکترهای غیرعددی و جستجو در رشته اعداد خالص.
        این روش شماره‌هایی مثل "0 9 1 2" یا "0-9-1-2" را هم پیدا می‌کند.
        """
        if not text: return []
        text = self._normalize_text(text)
        valid_phones = []

        # روش 1: پترن استاندارد (برای متن‌های تمیز)
        std_matches = re.findall(r'(?:\+98|0)?9\d{9}', text)
        for m in std_matches:
            clean = m.replace("+98", "0").lstrip("0")
            valid_phones.append("0" + clean)

        # روش 2: پترن خشن (حذف فاصله و خط تیره)
        # فقط کاراکترهای عدد و + را نگه می‌داریم
        digits_only = re.sub(r'[^0-9+]', '', text)
        
        # حالا در این رشته به دنبال شماره موبایل ایران می‌گردیم
        # پترن: 09xxxxxxxxx (11 رقم) یا 989xxxxxxxxx
        
        # جستجوی 09...
        matches_09 = re.findall(r'09\d{9}', digits_only)
        valid_phones.extend(matches_09)
        
        # جستجوی 989...
        matches_98 = re.findall(r'989\d{9}', digits_only)
        for m in matches_98:
            valid_phones.append("0" + m[2:])

        return list(set(valid_phones))

    def _save_data(self, record):
        """ذخیره امن در دیتابیس و اکسل"""
        # پر کردن فیلدهای خالی
        defaults = {"followers": "-", "following": "-", "posts": "-", "email": "-", "website": "", "bio": "", "fullname": record.get("username")}
        for k, v in defaults.items():
            if k not in record or not record[k]: record[k] = v

        try:
            success, msg = DatabaseHandler.save_record("instagram", record)
            if success:
                self.log(f"💾 ذخیره شد: {record['username']} | 📞 {record['phone']}", "success")
                return True
            else:
                self.log(f"⚠️ {msg}: {record['username']}", "warning")
                return False
        except Exception as e:
            self.log(f"❌ خطای ذخیره: {e}", "error")
            return False

    def _run_deep_core_engine(self, keyword, city, limit):
        self.log(f"🔥 موتور V21 (قدرت نهایی) روشن شد...", "info")
        
        if self.driver:
            try: self.driver.quit()
            except: pass
        
        self.driver = ScraperUtils.get_driver(headless=False)
        if not self.driver:
            self.btn_start.configure(state="normal")
            return

        self._apply_stealth()

        try:
            # =========================================================
            # PHASE 1: Google Harvesting (جمع‌آوری + شکار آنی)
            # =========================================================
            self.log(f"📥 فاز ۱: اسکن گوگل برای '{keyword}'...", "info")
            
            city_filter = f'"{city}"' if city else ""
            # کوئری بسیار دقیق برای اجبار گوگل به نمایش نتایج شماره‌دار
            # اضافه کردن 'OR "تماس"' و 'OR "سفارش"' شانس یافتن پیج‌های فروشگاهی را بالا می‌برد
            search_query = f'site:instagram.com "{keyword}" {city_filter} ("09" OR "+98" OR "تماس" OR "سفارش") -inurl:/p/ -inurl:/reel/'
            
            target_list = []
            hunted_count = 0
            page_num = 0
            processed_links = set()
            
            # حلقه جستجو تا رسیدن به تعداد
            while (len(target_list) + hunted_count) < limit and not self.stop_flag:
                start_index = page_num * 10
                # FIX: Clean URL without markdown formatting
                google_url = f"https://www.google.com/search?q={urllib.parse.quote(search_query)}&start={start_index}"
                
                self.driver.get(google_url)
                
                # دور زدن کپچا
                if "sorry" in self.driver.current_url:
                    self.log("⛔ کپچا گوگل! لطفاً حل کنید...", "error")
                    WebDriverWait(self.driver, 300).until(lambda d: "sorry" not in d.current_url)

                # استخراج با چندین سلکتور مختلف (برای اطمینان از دیده شدن همه نتایج)
                # div.g = استاندارد
                # div.MjjYud = باکس‌های جدید
                # div.Uk95Uc = نتایج تصویری/ویدئویی
                results = self.driver.find_elements(By.CSS_SELECTOR, "div.g, div.MjjYud, div.Uk95Uc")
                
                new_in_page = 0
                
                for res in results:
                    if (len(target_list) + hunted_count) >= limit: break
                    try:
                        # دریافت کل محتوای متنی و HTML برای تحلیل
                        full_text = res.text
                        full_html = res.get_attribute("innerHTML")
                        
                        # پیدا کردن لینک
                        href = ""
                        try: href = res.find_element(By.TAG_NAME, "a").get_attribute("href")
                        except: 
                            # فال‌بک: پیدا کردن لینک در HTML خام
                            hm = re.search(r'href="(https://www\.instagram\.com/[^"]+)"', full_html)
                            if hm: href = hm.group(1)

                        # استخراج یوزرنیم
                        u_match = re.search(r'instagram\.com/([A-Za-z0-9_.]+)/?', href)
                        if u_match:
                            username = u_match.group(1)
                            
                            # فیلتر تکراری و سیستمی
                            if username in ["p", "reels", "explore"] or href in processed_links: continue
                            if DatabaseHandler.is_duplicate("instagram", href): continue
                            
                            processed_links.add(href)
                            
                            # استخراج تایتل
                            try: title = res.find_element(By.TAG_NAME, "h3").text
                            except: title = username

                            # --- [تکنیک ۱] شکار آنی از گوگل (Instant Catch) ---
                            # ترکیب تایتل و توضیحات و جستجوی "جاروبرقی" برای شماره
                            combined_source = f"{title} {full_text}"
                            phones = self._vacuum_phones(combined_source)
                            
                            if phones:
                                record = {
                                    "username": username,
                                    "fullname": title,
                                    "bio": f"{full_text[:400]}... [Google Source]",
                                    "phone": phones[0], # اولین شماره پیدا شده
                                    "email": "Google Instant V21",
                                    "website": "Instagram",
                                    "category": keyword,
                                    "url": href
                                }
                                if self._save_data(record):
                                    hunted_count += 1
                                    new_in_page += 1
                                    continue # موفقیت! به نتیجه بعدی برو

                            # --- [تکنیک ۲] اضافه به صف برای بررسی عمیق ---
                            # اگر شماره در گوگل نبود، به لیست اضافه کن تا وارد پیج شویم
                            target_list.append({
                                "username": username,
                                "url": href,
                                "title": title,
                                "snippet": full_text
                            })
                            new_in_page += 1
                            self.log(f"➕ در صف بررسی: {username}", "info")

                    except Exception: continue

                if new_in_page == 0:
                    # اسکرول نهایی برای اطمینان
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(2)
                    if len(results) < 2:
                        self.log("⚠️ نتایج گوگل تمام شد.", "warning")
                        break
                
                page_num += 1
                time.sleep(random.uniform(2, 4))
            
            self.log(f"✅ فاز ۱ تکمیل. {hunted_count} شکار آنی. {len(target_list)} مورد برای بررسی عمیق.", "info")
            if not target_list: return

            # =========================================================
            # PHASE 2: Deep Core Mining (استخراج عمیق از سورس اینستاگرام)
            # =========================================================
            self.log(f"🕵️‍♂️ فاز ۲: نفوذ به {len(target_list)} پروفایل باقی‌مانده...", "info")
            
            for i, item in enumerate(target_list):
                if self.stop_flag: break
                username = item['username']
                self.log(f"[{i+1}/{len(target_list)}] ورود به پیج: {username}", "info")
                
                try:
                    # پاکسازی کوکی (حیاتی برای جلوگیری از 429)
                    self.driver.delete_all_cookies()
                    time.sleep(0.5)
                    self.driver.get(item['url'])
                    
                    # هندلینگ 429 (درخواست زیاد)
                    if "error 429" in self.driver.page_source.lower() or "wait" in self.driver.page_source.lower():
                         self.log("❄️ خنک‌سازی (45 ثانیه)...", "warning")
                         time.sleep(45)
                         self.driver.get(item['url'])

                    time.sleep(random.uniform(3, 5))
                    
                    # دریافت سورس کامل
                    page_source = self.driver.page_source
                    
                    # استخراج بیو از متادیتا (حتی اگر لاگین بخواهد)
                    bio_text = ""
                    
                    # 1. متادیتای OG (معمولا حاوی بیو است)
                    meta = re.search(r'<meta property="og:description" content="([^"]+)"', page_source)
                    if meta: bio_text += meta.group(1)
                    
                    # 2. استخراج از JSONهای مخفی (SharedData)
                    # اینستاگرام دیتای کامل پروفایل را در یک متغیر جاوا اسکریپت مخفی می‌کند
                    try:
                        # جستجوی کلید biography در سورس
                        json_match = re.search(r'"biography":"(.*?)"', page_source)
                        if json_match:
                            raw_bio = json_match.group(1)
                            # تبدیل یونیکد به متن (مثلا \u06...)
                            decoded_bio = bytes(raw_bio, 'utf-8').decode('unicode_escape')
                            bio_text += " " + decoded_bio
                    except: pass
                    
                    # ترکیب همه متون برای شکار نهایی
                    final_text = f"{bio_text} {item['snippet']} {item['title']}"
                    
                    # شکار شماره با جاروبرقی
                    phones = self._vacuum_phones(final_text)
                    
                    if phones:
                        record = {
                            "username": username,
                            "fullname": item['title'],
                            "bio": final_text[:500].replace("\n", " "),
                            "phone": phones[0],
                            "email": "Deep Core V21",
                            "website": "Instagram",
                            "category": keyword,
                            "url": item['url'],
                            "keyword": keyword # Added keyword
                        }
                        self._save_data(record)
                        hunted_count += 1
                    else:
                        self.log(f"❌ شماره‌ای یافت نشد: {username}", "error")

                    time.sleep(random.uniform(5, 8))

                except Exception as e:
                    self.log(f"خطای ارتباط: {e}", "error")

        except Exception as e:
            self.log(f"❌ خطای کلی: {e}", "error")
        finally:
            self.log(f"🏁 پایان. {hunted_count} شماره در لیست CRM ذخیره شد.", "success")
            self.btn_start.configure(state="normal")

class DivarUltimateFrame(BaseBotFrame):
    def __init__(self, master):
        super().__init__(master, "ربات دیوار پرو", "استخراج حرفه‌ای آگهی‌ها از سایت دیوار (نسخه هوشمند).")
        self.driver = None; self.stop_flag = False; self.force_start_processing = False
        self.setup_ui()
    
    def setup_ui(self):
        self.add_label("انتخاب مکان (استان یا شهر):")
        self.loc_var = ctk.StringVar(value="کل ایران")
        self.cmb_loc = self.add_combobox(list(LOCATION_MAP.keys()), variable=self.loc_var)
        self.cmb_loc.set("کل ایران")
        
        self.add_label("شهر دستی (فارسی یا فینگلیش):")
        self.entry_custom_city = self.add_entry("مثال: شیراز یا shiraz")
        
        self.add_label("کلمه کلیدی:")
        self.entry_keyword = self.add_entry("مثال: مبلمان")
        
        self.check_phone = self.add_checkbox("استخراج شماره تماس")
        self.check_phone.select()
        
        self.add_button("۱. ورود به حساب کاربری", self.open_login, "secondary")
        self.btn_start = self.add_button("۲. شروع استخراج", self.start_thread, "primary")
        self.btn_start.configure(state="disabled")
        
        # دکمه توقف اسکرول
        self.btn_skip = self.add_button("توقف اسکرول و شروع پردازش", self.skip_scrolling, "warning")
        self.btn_skip.configure(state="disabled")
        
        # دکمه توقف کامل
        self.add_button("توقف کامل عملیات", self.stop_process, "danger")
    
    def build_smart_url(self, user_input, location_slug):
        user_input = user_input.strip()
        base = "https://divar.ir"
        if "divar.ir" in user_input: 
            return "https://" + user_input.replace("https://", "").replace("http://", "")
        final_slug = location_slug if location_slug else "iran"
        
        if user_input: 
            return f"{base}/s/{final_slug}?q={urllib.parse.quote(user_input)}"
        return f"{base}/s/{final_slug}"
    
    def open_login(self): threading.Thread(target=self._login_logic).start()
    
    def _login_logic(self):
        try:
            if self.driver: 
                try: self.driver.quit()
                except: pass
            self.log("🌐 در حال باز کردن مرورگر...")
            self.driver = ScraperUtils.get_driver(headless=False)
            if not self.driver: return
            self.driver.get("https://divar.ir/my-divar/my-posts")
            self.log("لطفاً وارد حساب کاربری شوید.", "warning"); self.btn_start.configure(state="normal")
        except Exception as e: self.log(f"❌ خطا: {e}", "error")
    
    def start_thread(self):
        self.stop_flag = False; self.force_start_processing = False
        
        selected_loc = self.loc_var.get()
        raw_city = self.entry_custom_city.get().strip()
        kw = self.entry_keyword.get().strip()
        
        if raw_city:
            slug = get_city_slug(raw_city)
            self.log(f"📍 مکان از ورودی دستی تنظیم شد: {raw_city} -> {slug}", "info")
            prov_fa = raw_city
        else:
            slug = get_city_slug(selected_loc)
            self.log(f"📍 مکان انتخابی: {selected_loc} -> {slug}", "info")
            prov_fa = selected_loc
            
        url = self.build_smart_url(kw, slug)
        self.log(f"🔗 هدف نهایی: {url}", "info")
        
        self.btn_start.configure(state="disabled")
        self.btn_skip.configure(state="normal")
        threading.Thread(target=self.main_logic, args=(url, prov_fa, kw), daemon=True).start()
    
    def skip_scrolling(self): 
        self.force_start_processing = True 
        self.log("⚠️ اسکرول متوقف شد. در حال انتقال به مرحله پردازش آگهی‌ها...", "warning")
        
    def stop_process(self): 
        self.stop_flag = True 
        self.log("🛑 عملیات به طور کامل متوقف شد.", "error")
    
    def smart_wait_and_extract(self):
        """متد هوشمند انتظار برای ورود شماره و کد تایید پیامکی کاربر"""
        start_wait = time.time()
        contact_clicked = False
        
        while not self.stop_flag:
            try:
                is_blocked = False
                
                # 1. بررسی مودال ورود شماره موبایل (input name="mobile")
                try:
                    mobile_inputs = self.driver.find_elements(By.NAME, "mobile")
                    if mobile_inputs and any(i.is_displayed() for i in mobile_inputs):
                        self.log("⚠️ مرورگر منتظر شماست: لطفاً شماره موبایل خود را وارد کرده و تایید کنید...", "warning")
                        is_blocked = True
                except: pass

                # 2. بررسی مودال کد تایید پیامکی (input name="code")
                if not is_blocked:
                    try:
                        code_inputs = self.driver.find_elements(By.NAME, "code")
                        if code_inputs and any(i.is_displayed() for i in code_inputs):
                            self.log("⚠️ مرورگر منتظر شماست: لطفاً کد تایید ۶ رقمی را وارد کنید...", "warning")
                            is_blocked = True
                    except: pass
                
                # 3. بررسی کپچا
                if not is_blocked:
                    try:
                        captcha_elements = self.driver.find_elements(By.CLASS_NAME, "arc-puzzle")
                        if captcha_elements and any(c.is_displayed() for c in captcha_elements):
                            self.log("⚠️ کپچا شناسایی شد! لطفاً پازل را حل کنید...", "warning")
                            is_blocked = True
                    except: pass

                if is_blocked:
                    start_wait = time.time() 
                    time.sleep(2)
                    continue

                if not contact_clicked:
                    try:
                        btns = self.driver.find_elements(By.XPATH, "//button[contains(., 'اطلاعات تماس') or contains(., 'نمایش شماره') or contains(., 'تماس')]")
                        for btn in btns:
                            if btn.is_displayed():
                                ScraperUtils.smart_click(self.driver, btn)
                                contact_clicked = True
                                time.sleep(1.5)
                                break
                    except: pass

                try:
                    tels = self.driver.find_elements(By.XPATH, "//a[starts-with(@href, 'tel:')]")
                    if tels: 
                        return tels[0].get_attribute("href").replace("tel:", "")
                except: pass
                
                try:
                    body_txt = ScraperUtils.to_english_digits(self.driver.find_element(By.TAG_NAME, "body").text)
                    matches = re.findall(r'09\d{9}', body_txt)
                    if matches: return matches[0]
                except: pass
                
                if time.time() - start_wait > 10: 
                    return "Hidden"
                
                time.sleep(1)
            except Exception: 
                time.sleep(1)
            
        return "Hidden"
    
    def main_logic(self, url, province_name, keyword=""):
        if not self.driver: self.driver = ScraperUtils.get_driver(headless=False)
        if not self.driver: return
        collected_links = set()
        try:
            self.log("شروع جمع‌آوری آگهی‌ها...", "info"); self.driver.get(url); time.sleep(3)
            last_height = self.driver.execute_script("return document.body.scrollHeight"); no_change = 0
            
            while not self.stop_flag:
                if self.force_start_processing: 
                    break
                    
                elements = self.driver.find_elements(By.XPATH, "//a[contains(@href, '/v/')]")
                for el in elements:
                    try: 
                        h = el.get_attribute("href")
                        h = ScraperUtils.normalize_url("https://divar.ir", h)
                        if h and h not in collected_links and not DatabaseHandler.is_duplicate("divar", h): 
                            collected_links.add(h)
                    except: pass
                
                self.log(f"آگهی‌های جمع‌شده: {len(collected_links)}", "info")
                
                try:
                    btns = self.driver.find_elements(By.XPATH, "//button[contains(., 'بیشتر') or contains(., 'تلاش')]")
                    for b in btns:
                        if b.is_displayed(): ScraperUtils.smart_click(self.driver, b); time.sleep(1)
                except: pass
                
                ScraperUtils.human_scroll(self.driver)
                time.sleep(2)
                
                new_h = self.driver.execute_script("return document.body.scrollHeight")
                if new_h == last_height:
                    no_change += 1
                    if no_change > 4: break
                else: no_change = 0; last_height = new_h
                
                if len(collected_links) > 200: break

        except Exception as e: self.log(f"❌ خطا در فاز ۱: {e}", "error")
        
        self.btn_skip.configure(state="disabled"); total = len(collected_links)
        self.log(f"\n🚀 استخراج {total} آگهی...", "info"); links = list(collected_links)
        
        for i, link in enumerate(links):
            if self.stop_flag: break
            self.log(f"پردازش {i+1} از {total}", "info")
            try: self.process_ad(link, province_name, keyword); time.sleep(random.uniform(2.0, 5.0))
            except Exception as e: self.log(f"⚠️ خطای آگهی: {e}", "error")
        self.log("✅ عملیات پایان یافت.", "success"); self.btn_start.configure(state="normal")
    
    def process_ad(self, url, province_name, keyword=""):
        self.driver.execute_script(f"window.open('{url}', '_blank');"); 
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        data = {'ad_link': url, 'title': 'نامشخص', 'province': province_name, 'city': 'نامشخص', 'district': 'نامشخص', 'price': 'توافقی', 'phone': 'Hidden', 'website': 'نامشخص', 'email': 'نامشخص', 'address': 'نامشخص', 'description': '', 'keyword': keyword}
        try:
            self.driver.get(url)
            try: WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
            except: 
                self.log(f"⚠️ صفحه لود نشد: {url}", "warning")
                self.driver.close(); self.driver.switch_to.window(self.driver.window_handles[0])
                return

            try: data['title'] = self.driver.find_element(By.TAG_NAME, "h1").text
            except: pass
            
            try:
                subtitle_els = self.driver.find_elements(By.CLASS_NAME, "kt-page-title__subtitle")
                if subtitle_els:
                    subtitle_text = subtitle_els[0].text
                    if " در " in subtitle_text:
                        parts = subtitle_text.split(" در ")[1].split("،")
                        if len(parts) >= 1: data['city'] = parts[0].strip() 
                        if len(parts) >= 2: data['district'] = parts[1].strip() 
            except: pass
            
            try:
                rows = self.driver.find_elements(By.CLASS_NAME, "kt-group-row") or self.driver.find_elements(By.CLASS_NAME, "kt-base-row")
                for row in rows:
                    txt = ScraperUtils.clean_text_for_excel(row.text)
                    if "قیمت" in txt: data['price'] = txt.replace("قیمت", "").strip()
            except: pass
            
            if self.check_phone.get():
                ph = self.smart_wait_and_extract()
                if ph and ph != "Hidden": data['phone'] = ph
            
            if data['phone'] == 'Hidden': 
                self.log("⏭️ شماره مخفی بود.", "info")
            else:
                success, msg = DatabaseHandler.save_record("divar", data)
                if success: self.log(f"💾 ذخیره شد: {data['phone']}", "success")
                else: self.log(f"⚠️ {msg}: {data['phone']}", "warning")
                
        finally: 
            try:
                self.driver.close() 
                self.driver.switch_to.window(self.driver.window_handles[0])
            except: pass

class SheypoorUltimateFrame(BaseBotFrame):
    def __init__(self, master):
        super().__init__(master, "ربات شیپور پرو", "استخراج حرفه‌ای آگهی‌ها از سایت شیپور (نسخه هوشمند).")
        self.driver = None; self.stop_flag = False; self.force_start_processing = False
        self.setup_ui()
    
    def setup_ui(self):
        self.add_label("انتخاب مکان (استان یا شهر):")
        self.loc_var = ctk.StringVar(value="کل ایران")
        self.cmb_loc = self.add_combobox(list(LOCATION_MAP.keys()), variable=self.loc_var)
        self.cmb_loc.set("کل ایران")
        
        self.add_label("شهر دستی (فارسی یا فینگلیش):")
        self.ent_city = self.add_entry("مثال: شیراز یا shiraz")
        
        self.add_label("کلمه کلیدی:")
        self.ent_kw = self.add_entry("خودرو")
        
        self.check_phone = self.add_checkbox("استخراج شماره تماس")
        self.check_phone.select()
        
        self.add_button("۱. ورود به حساب کاربری", self.login, "secondary")
        self.btn_start = self.add_button("۲. شروع استخراج", self.start, "primary")
        self.btn_start.configure(state="disabled")
        
        # دکمه توقف اسکرول
        self.btn_skip = self.add_button("توقف اسکرول و شروع پردازش", self.skip_scrolling, "warning")
        self.btn_skip.configure(state="disabled")
        
        # دکمه توقف کامل
        self.add_button("توقف کامل عملیات", self.stop_process, "danger")
    
    def build_sheypoor_url(self, keyword, city_slug):
        keyword = keyword.strip()
        city_slug = city_slug.strip() if city_slug else "iran"
        if "sheypoor.com" in keyword: 
            return "https://" + keyword if not keyword.startswith("http") else keyword
        if keyword: 
            return f"https://www.sheypoor.com/s/{city_slug}?q={urllib.parse.quote(keyword)}"
        return f"https://www.sheypoor.com/s/{city_slug}"
    
    def login(self): threading.Thread(target=self._login_t).start()
    
    def _login_t(self):
        self.log("🌐 باز کردن مرورگر...", "info"); 
        if self.driver: 
            try: self.driver.quit()
            except: pass
        self.driver = ScraperUtils.get_driver()
        if not self.driver: return
        self.driver.get("https://www.sheypoor.com/session")
        self.log("لطفاً وارد شوید.", "warning"); self.btn_start.configure(state="normal")
    
    def start(self):
        self.stop_flag = False; self.force_start_processing = False
        
        selected_loc = self.loc_var.get()
        raw_city = self.ent_city.get().strip()
        kw = self.ent_kw.get().strip()
        
        if raw_city:
            city_slug = get_city_slug(raw_city)
            self.log(f"📍 مکان از ورودی دستی تنظیم شد: {raw_city} -> {city_slug}", "info")
        else:
            city_slug = get_city_slug(selected_loc)
            self.log(f"📍 مکان انتخابی: {selected_loc} -> {city_slug}", "info")
             
        url = self.build_sheypoor_url(kw, city_slug)
        self.log(f"🔗 هدف نهایی: {url}", "info")
        
        self.btn_start.configure(state="disabled")
        self.btn_skip.configure(state="normal")
        threading.Thread(target=self._run, args=(url, kw)).start()
    
    def skip_scrolling(self): 
        self.force_start_processing = True 
        self.log("⚠️ اسکرول متوقف شد. در حال انتقال به مرحله پردازش...", "warning")
        
    def stop_process(self): 
        self.stop_flag = True 
        self.log("🛑 عملیات به طور کامل متوقف شد.", "error")
    
    def extract_phone_targeted(self):
        start_wait = time.time()
        while not self.stop_flag:
            try:
                blockers = self.driver.find_elements(By.NAME, "code") + \
                           self.driver.find_elements(By.XPATH, "//div[contains(text(), 'کد امنیتی') or contains(text(), 'ورود')]")
                
                visible_blockers = [b for b in blockers if b.is_displayed()]
                if visible_blockers:
                    start_wait = time.time() # جلوگیری از تایم‌اوت در صورت مسدود شدن
                    self.log("⚠️ توقف موقت: لطفا کد امنیتی یا ورود را انجام دهید...", "warning")
                    time.sleep(3)
                    continue
                
                full_html = ScraperUtils.convert_persian_digits(self.driver.page_source)
                matches = re.findall(r'(09\d{9})', full_html)
                valid_phones = [m for m in matches if not m.startswith('0900')]
                if valid_phones: return valid_phones[-1]
                
                if time.time() - start_wait > 8: return "Hidden"

                try:
                    contact_btns = self.driver.find_elements(By.XPATH, "//button[contains(., 'تماس') or contains(., 'اطلاعات') or contains(., 'نمایش')]")
                    for btn in contact_btns:
                        if btn.is_displayed():
                            ScraperUtils.smart_click(self.driver, btn)
                            time.sleep(1)
                            break
                except: pass
                
                time.sleep(0.5)
            except: time.sleep(0.5)
        return "Hidden"

    def _run(self, url, keyword=""):
        if not self.driver: self.driver = ScraperUtils.get_driver()
        if not self.driver: return
        self.driver.get(url); time.sleep(3); collected_links = set()
        
        while not self.stop_flag:
            if self.force_start_processing: 
                break
                
            try:
                links = self.driver.find_elements(By.XPATH, "//a[contains(@href, '/v/')]")
                for el in links:
                    h = el.get_attribute("href")
                    h = ScraperUtils.normalize_url("https://www.sheypoor.com", h)
                    if h and "sheypoor.com/v/" in h and not DatabaseHandler.is_duplicate("sheypoor", h):
                        collected_links.add(h)
            except: pass
            
            self.log(f"آگهی‌های: {len(collected_links)}", "info")
            ScraperUtils.human_scroll(self.driver)
            
            if len(self.driver.find_elements(By.NAME, "code")) > 0:
                self.log("⛔ کپچا در لیست! حل کنید...", "warning")
                time.sleep(10)
                
            if len(collected_links) > 100: break

        self.btn_skip.configure(state="disabled"); links = list(collected_links)
        self.log(f"\n🚀 استخراج {len(links)} آگهی...", "info")
        
        for i, link in enumerate(links):
            if self.stop_flag: break
            self.log(f"پردازش {i+1} از {len(links)}", "info")
            try: self.process_ad(link, keyword); time.sleep(random.uniform(3.0, 6.0))
            except Exception as e: self.log(f"خطا: {e}", "error")
            
        self.log("✅ پایان عملیات.", "success"); self.btn_start.configure(state="normal")
        
    def process_ad(self, url, keyword=""):
        self.driver.execute_script(f"window.open('{url}', '_blank');"); 
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        data = {'ad_link': url, 'title': 'نامشخص', 'province': 'نامشخص', 'city': 'نامشخص', 'district': 'نامشخص', 'price': 'توافقی', 'phone': 'Hidden', 'description': '', 'address': 'نامشخص', 'email': 'نامشخص', 'website': 'نامشخص', 'keyword': keyword}
        try:
            self.driver.get(url); wait = WebDriverWait(self.driver, 10)
            try: data['title'] = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
            except: 
                self.driver.close(); self.driver.switch_to.window(self.driver.window_handles[0])
                return
            
            if self.check_phone.get(): data['phone'] = self.extract_phone_targeted()
            
            if data['phone'] != 'Hidden':
                success, msg = DatabaseHandler.save_record("sheypoor", data)
                if success: self.log(f"💾 ذخیره: {data['phone']}", "success")
                else: self.log(f"⚠️ {msg}: {data['phone']}", "warning")
            else: self.log(f"⏭️ بدون شماره.", "info")
            
        finally:
            if len(self.driver.window_handles) > 1: 
                self.driver.close(); self.driver.switch_to.window(self.driver.window_handles[0])

class NeshanUltimateFrame(BaseBotFrame):
    def __init__(self, master):
        super().__init__(master, "ربات نشان پرو (اصلاح شده)", "جستجو بر اساس شهر و کلمه کلیدی با استخراج دقیق.")
        self.stop_flag = False
        self.driver = None
        self.setup_ui()

    def setup_ui(self):
        self.add_label("شهر (مثال: تهران):")
        self.ent_city = self.add_entry("تهران")
        self.add_label("کلمه کلیدی (مثال: سالن زیبایی):")
        self.ent_kw = self.add_entry("سالن زیبایی")
        self.btn_start = self.add_button("🚀 شروع جستجو و استخراج", self.start, "primary")
        self.add_button("توقف عملیات", self.stop, "danger")

    def start(self): 
        city = self.ent_city.get().strip()
        kw = self.ent_kw.get().strip()
        if not city or not kw:
            messagebox.showerror("خطا", "لطفاً هم شهر و هم کلمه کلیدی را وارد کنید.")
            return
        self.stop_flag = False
        self.btn_start.configure(state="disabled")
        threading.Thread(target=self._run, args=(city, kw)).start()

    def stop(self): 
        self.stop_flag = True
        self.log("🛑 دستور توقف صادر شد.", "error")

    def _run(self, city, keyword):
        search_term = f"{keyword} {city}"
        self.log(f"🌍 در حال باز کردن نشان برای: {search_term}", "info")
        self.driver = ScraperUtils.get_driver()
        if not self.driver: 
            self.btn_start.configure(state="normal")
            return

        try:
            encoded_query = urllib.parse.quote(search_term)
            target_url = f"https://neshan.org/maps/search/{encoded_query}"
            
            self.driver.get(target_url)
            wait = WebDriverWait(self.driver, 20)
            
            self.log("⏳ در حال بارگذاری لیست...", "info")
            # Wait for list or pins
            try: wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/maps/places/')]")))
            except: 
                self.log("⚠️ نتیجه‌ای یافت نشد.", "warning")
                self.btn_start.configure(state="normal")
                return

            collected_data = [] 
            seen_links = set()
            no_new_data_count = 0
            
            while not self.stop_flag:
                elements = self.driver.find_elements(By.XPATH, "//a[contains(@href, '/maps/places/')]")
                new_found = False
                for el in elements:
                    try:
                        link = el.get_attribute("href")
                        if "?" in link: link = link.split("?")[0]
                        if link not in seen_links:
                            name = el.text.split('\n')[0] if el.text else "نامشخص"
                            if len(name) > 2: 
                                seen_links.add(link)
                                collected_data.append({'name': name, 'url': link})
                                new_found = True
                    except: pass
                
                self.log(f"📦 تعداد {len(collected_data)} مکان پیدا شد...", "info")
                if not new_found: no_new_data_count += 1
                else: no_new_data_count = 0
                
                if no_new_data_count > 3: break
                if len(collected_data) >= 40: break # Reasonable limit
                
                if elements:
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", elements[-1])
                time.sleep(2)

            self.log(f"🔍 شروع استخراج جزئیات از {len(collected_data)} مورد...", "info")
            
            for i, item in enumerate(collected_data):
                if self.stop_flag: break
                if DatabaseHandler.is_duplicate("neshan", item['url']): continue
                
                self.log(f"بازدید ({i+1}/{len(collected_data)}): {item['name']}", "info")
                try:
                    self.driver.get(item['url'])
                    
                    # [MODIFIED] انتظار هوشمند برای لود کامل (تایتل یا کلاس‌های تماس)
                    try:
                        WebDriverWait(self.driver, 15).until(
                            lambda d: d.find_elements(By.CLASS_NAME, "SWIQUYQ") or \
                                      d.find_elements(By.CLASS_NAME, "TR71vO0") or \
                                      d.find_elements(By.TAG_NAME, "h1")
                        )
                    except: pass
                    
                    time.sleep(2.5) # اطمینان از رندر کامل JS
                    
                    phone = "Hidden"
                    
                    # استراتژی ۱: استخراج مستقیم از متن (کلاس SWIQUYQ)
                    # <p class="SWIQUYQ">...<span>شماره تماس: 021...</span></p>
                    try:
                        info_paragraphs = self.driver.find_elements(By.CLASS_NAME, "SWIQUYQ")
                        for p in info_paragraphs:
                            if "شماره تماس" in p.text:
                                raw_text = p.text
                                # پاکسازی: حذف همه چیز جز عدد
                                digits = re.sub(r'[^0-9]', '', ScraperUtils.to_english_digits(raw_text))
                                if len(digits) >= 8:
                                    phone = digits
                                    # اصلاح فرمت (مثلاً 2188... به 02188...)
                                    if not phone.startswith("0"): phone = "0" + phone
                                    break
                    except: pass
                    
                    # استراتژی ۲: کلیک روی دکمه تماس (کلاس TR71vO0)
                    # <button class="TR71vO0">...<span>تماس</span></button>
                    if phone == "Hidden":
                        try:
                            contact_btns = self.driver.find_elements(By.CLASS_NAME, "TR71vO0")
                            for btn in contact_btns:
                                if "تماس" in btn.text:
                                    ScraperUtils.smart_click(self.driver, btn)
                                    time.sleep(1.5)
                                    
                                    # بررسی اینکه آیا لینک tel ظاهر شد؟
                                    try:
                                        tels = self.driver.find_elements(By.XPATH, "//a[starts-with(@href, 'tel:')]")
                                        if tels:
                                            raw = tels[0].get_attribute("href").replace("tel:", "")
                                            clean = ScraperUtils.to_english_digits(raw).replace("+98", "0")
                                            clean = re.sub(r'[^0-9]', '', clean)
                                            if len(clean) >= 8: phone = clean
                                    except: pass
                                    break
                        except: pass
                    
                    # استراتژی ۳: فال‌بک نهایی (جستجو در کل متن)
                    if phone == "Hidden":
                        try:
                            body = self.driver.find_element(By.TAG_NAME, "body").text
                            phones = ScraperUtils.extract_phones_aggressive(body)
                            if phones: phone = phones[0]
                        except: pass

                    address = "نامشخص"
                    try:
                        # Extract address from text
                        body = self.driver.find_element(By.TAG_NAME, "body").text
                        for line in body.split("\n"):
                            if city in line and len(line) > len(city) + 5:
                                address = line
                                break
                    except: pass

                    record = {
                        "name": item['name'], "phone": phone, "category": keyword,
                        "address": address, "website": "نامشخص", "email": "نامشخص",
                        "hours": "نامشخص", "keyword": search_term, "unique_id": item['url']
                    }
                    success, msg = DatabaseHandler.save_record("neshan", record)
                    if success: self.log(f"💾 ذخیره شد: {phone}", "success")
                    else: self.log(f"⚠️ {msg}", "warning")
                    
                except Exception as e:
                    self.log(f"خطا در آیتم: {e}", "error")

        except Exception as e:
            self.log(f"❌ خطای کلی: {e}", "error")
        finally:
            self.log("پایان عملیات نشان.", "success")
            self.btn_start.configure(state="normal")
            if self.driver:
                try: self.driver.quit()
                except: pass

class NiazroozUltimateFrame(BaseBotFrame):
    def __init__(self, master):
        super().__init__(master, "ربات نیازروز", "استخراج آگهی‌ها از سایت نیازروز.")
        self.stop_flag = False; self.driver = None; self.setup_ui()

    def setup_ui(self):
        self.add_label("کلمه کلیدی:")
        self.ent_kw = self.add_entry("لوله بازکنی")
        self.add_label("تعداد صفحات (خالی = همه):")
        self.ent_pages = self.add_entry("5") 
        self.ent_pages.delete(0, 'end'); self.ent_pages.insert(0, "5")
        self.add_button("شروع استخراج", self.start, "primary")
        self.add_button("توقف عملیات", self.stop, "danger")

    def start(self): 
        self.stop_flag = False
        limit_str = self.ent_pages.get().strip()
        limit = int(limit_str) if limit_str.isdigit() else 999999
        threading.Thread(target=self._run, args=(limit,)).start()

    def stop(self): self.stop_flag = True

    def _run(self, page_limit):
        keyword = self.ent_kw.get().strip()
        if not keyword: return
        self.log(f"🚀 شروع پردازش برای: {keyword}", "info")
        self.driver = ScraperUtils.get_driver()
        if not self.driver: return

        collected_links = []
        page = 1
        
        self.log("📋 فاز ۱: جمع‌آوری لینک‌ها...", "info")
        try:
            while page <= page_limit and not self.stop_flag:
                url = f"https://www.niazerooz.com/keys/{urllib.parse.quote(keyword)}?page={page}"
                self.log(f"📄 بررسی صفحه {page}...", "info")
                self.driver.get(url)
                try: WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'order-box')))
                except: 
                    self.log("🏁 پایان صفحات یا عدم یافتن نتیجه.", "warning"); break
                
                ads = self.driver.find_elements(By.CSS_SELECTOR, '.order-box .ob-subject a')
                new_links = 0
                for ad in ads:
                    try:
                        href = ad.get_attribute('href')
                        clean_href = ScraperUtils.normalize_url("https://www.niazerooz.com", href)
                        if clean_href and clean_href not in collected_links:
                             if not DatabaseHandler.is_duplicate("niazrooz", clean_href):
                                 collected_links.append(clean_href)
                                 new_links += 1
                    except: pass
                self.log(f"➕ {new_links} لینک جدید یافت شد.", "success")
                if new_links == 0 and page > 1:
                    self.log("⚠️ تکراری یا پایان لیست.", "warning"); break
                page += 1
                time.sleep(random.uniform(2, 4))
        except Exception as e:
            self.log(f"❌ خطا در جمع‌آوری لینک: {e}", "error")

        total = len(collected_links)
        self.log(f"\n🚀 فاز ۲: استخراج اطلاعات از {total} آگهی...", "info")
        for i, link in enumerate(collected_links):
            if self.stop_flag: break
            self.log(f"پردازش {i+1} از {total}", "info")
            try:
                self.process_ad_detail(link, keyword) # Pass KW
                time.sleep(random.uniform(3, 6))
            except Exception as e:
                self.log(f"⚠️ خطا در لینک {i+1}: {e}", "error")
        self.log("✅ عملیات پایان یافت.", "success")
        if self.driver: self.driver.quit()

    def process_ad_detail(self, url, keyword=""):
        self.driver.get(url)
        data = {'title': 'نامشخص', 'owner': 'نامشخص', 'phone': 'Hidden', 'email': 'نامشخص', 'website': 'نامشخص', 'address': 'نامشخص', 'whatsapp': 'نامشخص', 'ad_link': url, 'keyword': keyword}
        try:
            try: data['title'] = self.driver.find_element(By.TAG_NAME, "h1").text.strip()
            except: pass
            try:
                contact_box = self.driver.find_element(By.CLASS_NAME, "order-contactbox")
                try: 
                    name_el = contact_box.find_element(By.CSS_SELECTOR, ".order-contactbox__name strong")
                    data['owner'] = name_el.text.strip()
                except: pass
                phones = []
                try:
                    mobile_text = contact_box.find_element(By.CSS_SELECTOR, ".order-contactbox__mobile-text strong").text
                    phones.append(ScraperUtils.to_english_digits(mobile_text))
                except: pass
                links = contact_box.find_elements(By.TAG_NAME, "a")
                for a in links:
                    href = a.get_attribute("href")
                    if not href: continue
                    if href.startswith("tel:"): phones.append(ScraperUtils.to_english_digits(href.replace("tel:", "")))
                    elif href.startswith("sms:"): phones.append(ScraperUtils.to_english_digits(href.replace("sms:", "")))
                    elif "wa.me" in href or "whatsapp" in href: data['whatsapp'] = href
                data['phone'] = ", ".join(ScraperUtils.uniq(phones)) if phones else "Hidden"
            except: pass
            try:
                rows = self.driver.find_elements(By.CLASS_NAME, "order-links__row-item")
                for row in rows:
                    txt = row.text
                    if "ایمیل:" in txt:
                        try:
                            email_el = row.find_element(By.CSS_SELECTOR, "a[href^='mailto:']")
                            data['email'] = email_el.get_attribute("href").replace("mailto:", "").strip()
                        except: pass
                    if "وبسایت:" in txt:
                        try:
                            web_el = row.find_element(By.CSS_SELECTOR, "a")
                            href = web_el.get_attribute("href")
                            if href and "mailto" not in href: data['website'] = href
                        except: pass
            except: pass
            try:
                body_text = self.driver.find_element(By.TAG_NAME, "body").text
                for line in body_text.split('\n'):
                    if "آدرس:" in line:
                         data['address'] = line.replace("آدرس:", "").strip(); break
            except: pass

            if data['phone'] != 'Hidden':
                 success, msg = DatabaseHandler.save_record("niazrooz", data)
                 if success: self.log(f"💾 ذخیره: {data['owner']} - {data['phone']}", "success")
                 else: self.log(f"⚠️ {msg}: {data['phone']}", "warning")
            else:
                 self.log(f"⏭️ بدون شماره: {data['title']}", "warning")
        except Exception as e:
            self.log(f"خطا در پارس صفحه: {e}", "error")

class MapsUltimateFrame(BaseBotFrame):
    def __init__(self, master):
        super().__init__(master, "ربات گوگل مپس (لینک مستقیم)", "استخراج دقیق از گوگل مپس با تولید لینک جستجوی پیشرفته.")
        self.stop_flag = False; self.driver = None; self.setup_ui()
    def setup_ui(self):
        self.add_label("مکان:"); self.ent_loc = self.add_entry("Tehran")
        self.add_label("کلمات کلیدی (کاما):"); self.ent_kw = self.add_entry("Restaurant, Cafe")
        self.btn_start = self.add_button("شروع استخراج", self.start, "primary")
        self.add_button("توقف عملیات", self.stop_process, "danger")
    def start(self): 
        if not self.ent_loc.get() or not self.ent_kw.get(): return
        self.stop_flag = False; self.btn_start.configure(state="disabled")
        threading.Thread(target=self._run, args=(self.ent_loc.get().strip(), self.ent_kw.get().strip())).start()
    def stop_process(self): self.stop_flag = True; self.log("⛔ توقف...", "error")
    
    def _run(self, location, keywords_raw):
        kw_list = [k.strip() for k in keywords_raw.replace('\n', ',').split(',') if k.strip()]
        try:
            self.log("🔧 راه‌اندازی مرورگر...", "info"); self.driver = ScraperUtils.get_driver() 
            if not self.driver: 
                self.btn_start.configure(state="normal")
                return
            
            wait = WebDriverWait(self.driver, 20)
            
            for kw in kw_list:
                if self.stop_flag: break
                
                # --- تغییر اصلی: ساخت لینک مستقیم جستجو ---
                search_term = f"{kw} {location}"
                encoded_query = urllib.parse.quote(search_term)
                # اضافه کردن hl=en برای یکسان‌سازی زبان (Selectors)
                target_url = f"https://www.google.com/maps/search/{encoded_query}?hl=en&entry=ttu"
                
                self.log(f"\n🔎 هدایت به: {target_url}", "info")
                
                try:
                    self.driver.get(target_url)
                    
                    # 3. انتظار هوشمند برای نتایج
                    self.log("⏳ منتظر لیست نتایج...", "info")
                    
                    # بررسی می‌کنیم یا لیست (feed) ظاهر شود یا یک نتیجه تکی (h1)
                    try:
                        wait.until(lambda d: d.find_elements(By.CSS_SELECTOR, "div[role='feed']") or d.find_elements(By.CSS_SELECTOR, "h1.DUwDvf"))
                    except:
                        self.log("⚠️ نتیجه‌ای یافت نشد یا لود نشد.", "warning")
                        continue
                        
                    time.sleep(3)
                    
                except Exception as e: 
                    self.log(f"خطا در لود صفحه: {e}", "error")
                    continue
                
                self.log("📜 اسکرول لیست...", "info"); links = set(); consecutive_fails = 0
                
                # Scroll Loop
                while not self.stop_flag:
                    try:
                        # Find main feed
                        feeds = self.driver.find_elements(By.CSS_SELECTOR, "div[role='feed']")
                        
                        # اگر فید پیدا نشد، شاید فقط یک نتیجه است (Single Result)
                        if not feeds:
                            # بررسی اینکه آیا واقعاً یک نتیجه باز شده است؟
                            if len(self.driver.find_elements(By.CSS_SELECTOR, "h1.DUwDvf")) > 0:
                                self.log("📍 تک نتیجه یافت شد.", "info")
                                if self.driver.current_url not in links:
                                    links.add(self.driver.current_url)
                            break
                            
                        feed = feeds[0]
                        
                        # Find elements (New Selector: a.hfpxzc is the invisible link covering the card)
                        elements = feed.find_elements(By.CSS_SELECTOR, "a.hfpxzc")
                        current_len = len(elements)
                        
                        for el in elements:
                            href = el.get_attribute("href")
                            if href and href not in links:
                                if not DatabaseHandler.is_duplicate("maps", href): links.add(href)
                        
                        # Scroll the FEED, not the window
                        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", feed)
                        time.sleep(2.5)
                        
                        # Check if new loaded
                        new_elements = feed.find_elements(By.CSS_SELECTOR, "a.hfpxzc")
                        if len(new_elements) == current_len:
                            consecutive_fails += 1
                            # Look for "You've reached the end" message
                            try: self.driver.find_element(By.CSS_SELECTOR, "span.HlvSq"); break 
                            except: pass
                            
                            if consecutive_fails > 3: break
                        else: consecutive_fails = 0
                        
                        self.log(f"یافت شد: {len(links)} مورد...", "info")
                        if len(links) >= 60: break
                        
                    except Exception as e: 
                        self.log(f"اسکرول متوقف شد: {e}", "warning")
                        break
                
                # Extraction Loop
                for i, link in enumerate(links):
                    if self.stop_flag: break
                    self.log(f"پردازش: {i+1} از {len(links)}", "info")
                    try:
                        self.driver.get(link); time.sleep(random.uniform(2.0, 4.0))
                        
                        name = ""; cat = ""; addr = ""; ph = ""; web = ""
                        
                        try: name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.DUwDvf"))).text
                        except: pass
                        
                        if not name: continue
                        
                        try: cat = self.driver.find_element(By.CSS_SELECTOR, "button[jsaction*='category']").text
                        except: pass
                        
                        try: addr = self.driver.find_element(By.CSS_SELECTOR, "button[data-item-id='address']").get_attribute("aria-label").replace("Address: ", "").replace("آدرس: ", "").strip()
                        except: pass
                        
                        try: 
                            # Phone usually has data-item-id starting with phone:
                            ph_btn = self.driver.find_element(By.CSS_SELECTOR, "button[data-item-id^='phone']")
                            ph = ph_btn.get_attribute("aria-label").replace("Phone: ", "").replace("تلفن: ", "").strip()
                        except: pass
                        
                        try: web = self.driver.find_element(By.CSS_SELECTOR, "a[data-item-id='authority']").get_attribute("href")
                        except: pass
                        
                        success, msg = DatabaseHandler.save_record("maps", {"keyword": kw, "business_name": name, "category": cat, "address": addr, "phone": ph, "website": web, "email": "نامشخص", "hours": "", "unique_id": link})
                        if success: self.log(f"✅ ذخیره: {name}", "success")
                        
                    except Exception as e:
                        self.log(f"خطا در استخراج: {e}", "warning")
                        
        except Exception as e: self.log(f"❌ خطا: {e}", "error")
        finally:
            if self.driver: self.driver.quit()
            self.btn_start.configure(state="normal"); self.log("پایان عملیات.", "success")

class AvvalUltimateFrame(BaseBotFrame):
    def __init__(self, master):
        super().__init__(master, "ربات اول (Avval.ir)", "استخراج اطلاعات از کتاب اول.")
        self.driver = None; self.stop_flag = False; self.setup_ui()
    def setup_ui(self):
        self.add_label("شهر:"); self.ent_city = self.add_entry("مثال: تهران")
        self.add_label("کلمه کلیدی:"); self.ent_kw = self.add_entry("مثال: پزشک")
        self.add_label("تعداد صفحات:"); self.ent_pages = self.add_entry("مثال: 5"); self.ent_pages.insert(0, "5")
        self.btn_start = self.add_button("شروع استخراج", self.start, "primary")
        self.add_button("توقف عملیات", self.stop_process, "danger")
    def start(self):
        if not self.ent_city.get() or not self.ent_kw.get(): return
        self.stop_flag = False; self.btn_start.configure(state="disabled")
        try: num_pages = int(self.ent_pages.get())
        except: num_pages = 5
        threading.Thread(target=self._run, args=(self.ent_city.get().strip(), self.ent_kw.get().strip(), num_pages)).start()
    def stop_process(self): self.stop_flag = True; self.log("⛔ توقف...", "error")
    def _run(self, city, keyword, num_pages):
        try:
            self.log("🔧 راه‌اندازی مرورگر...", "info"); self.driver = ScraperUtils.get_driver(); 
            if not self.driver: return
            kw_slug = keyword.strip().replace(" ", "-"); city_slug = city.strip().replace(" ", "-"); base_url = f"https://avval.ir/search/{quote(kw_slug)}-%D8%AF%D8%B1-{quote(city_slug)}"
            for page in range(1, num_pages + 1):
                if self.stop_flag: break
                url = base_url if page == 1 else f"{base_url}?page={page}"
                self.log(f"📄 دریافت صفحه {page}...", "info"); self.driver.get(url)
                try: WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "content")))
                except: break
                items = self.driver.find_elements(By.CLASS_NAME, "content")
                if not items: break
                ScraperUtils.human_scroll(self.driver)
                for item in items:
                    if self.stop_flag: break
                    try:
                        try: title = item.find_element(By.TAG_NAME, "h2").text.strip()
                        except: title = "نامشخص"
                        try: link = item.find_element(By.TAG_NAME, "a").get_attribute("href")
                        except: link = url 
                        link = ScraperUtils.normalize_url("https://avval.ir", link)
                        if DatabaseHandler.is_duplicate("avval", link): continue
                        phone_str = "نامشخص"
                        try:
                            seq_div = item.find_element(By.CLASS_NAME, "sequence")
                            phones = [s.text.strip() for s in seq_div.find_elements(By.TAG_NAME, "span") if s.text.strip()]
                            if phones: phone_str = " | ".join(phones)
                        except: pass
                        success, msg = DatabaseHandler.save_record("avval", {"title": title, "city": city, "category": "General", "address": "نامشخص", "phone": phone_str, "email": "نامشخص", "website": "نامشخص", "keyword": keyword, "url": link})
                        if success: self.log(f"✅ استخراج شد: {title}", "success")
                    except: pass
                time.sleep(random.uniform(3, 6))
        except Exception as e: self.log(f"❌ خطا: {e}", "error")
        finally:
            if self.driver: self.driver.quit()
            self.btn_start.configure(state="normal"); self.log("پایان عملیات.", "success")


class IranTejaratUltimateFrame(BaseBotFrame):
    def __init__(self, master):
        super().__init__(master, "ربات ایران تجارت (ساختار جدید)", "استخراج سریع اطلاعات از باکس‌های جستجو طبق ساختار HTML جدید.")
        self.driver = None
        self.stop_flag = False
        self.setup_ui()

    def setup_ui(self):
        self.add_label("کلمه کلیدی (مثال: سمپاشی):")
        self.ent_kw = self.add_entry("سمپاشی")
        
        self.add_label("تعداد صفحات برای بررسی:")
        self.ent_pages = self.add_entry("5")
        
        self.btn_start = self.add_button("🚀 شروع استخراج سریع", self.start, "primary")
        self.add_button("توقف عملیات", self.stop_process, "danger")

    def start(self):
        kw = self.ent_kw.get().strip()
        if not kw:
            messagebox.showerror("خطا", "لطفاً کلمه کلیدی را وارد کنید.")
            return
            
        try:
            limit = int(self.ent_pages.get())
        except:
            limit = 5
            
        self.stop_flag = False
        self.btn_start.configure(state="disabled")
        threading.Thread(target=self._run, args=(kw, limit)).start()

    def stop_process(self): 
        self.stop_flag = True
        self.log("⛔ دستور توقف ارسال شد...", "error")
    
    def _run(self, keyword, page_limit):
        try:
            self.log("🔧 راه‌اندازی مرورگر...", "info")
            self.driver = ScraperUtils.get_driver()
            if not self.driver: 
                self.btn_start.configure(state="normal")
                return

            # انکود کلمه کلیدی
            encoded_kw = urllib.parse.quote_plus(keyword)
            
            for page in range(1, page_limit + 1):
                if self.stop_flag: break
                
                # ساخت لینک
                if page == 1:
                    current_url = f"https://iran-tejarat.com/SearchResult/SearchResult.html/k={encoded_kw}"
                else:
                    page_index = page - 1
                    current_url = f"https://iran-tejarat.com/SearchResultPage{page_index}/SearchResult.html/k={encoded_kw}"
                
                self.log(f"📄 در حال پردازش صفحه {page}...", "info")
                self.log(f"لینک: {current_url}", "info")
                
                try:
                    self.driver.get(current_url)
                    time.sleep(3)
                    
                    if "نتیجه ای یافت نشد" in self.driver.page_source:
                        self.log("⚠️ به پایان نتایج رسیدیم.", "warning")
                        break
                except Exception as e:
                    self.log(f"خطا در باز کردن صفحه: {e}", "error")
                    continue

                # --- تغییر اصلی: استفاده از کلاس singlesearch به عنوان کانتینر ---
                ad_containers = self.driver.find_elements(By.CLASS_NAME, "singlesearch")
                
                if not ad_containers:
                    self.log("⚠️ هیچ باکسی با کلاس singlesearch یافت نشد.", "warning")
                    continue

                self.log(f"📦 تعداد {len(ad_containers)} آگهی یافت شد. استخراج...", "info")
                
                new_count = 0
                for box in ad_containers:
                    if self.stop_flag: break
                    try:
                        # 1. استخراج عنوان و لینک (AlhtitleForSearch)
                        title = "نامشخص"
                        url = current_url
                        try:
                            # طبق HTML شما: <div class="AlhtitleForSearch"><a ...><h2>...</h2></a></div>
                            link_el = box.find_element(By.CSS_SELECTOR, ".AlhtitleForSearch a")
                            href = link_el.get_attribute("href")
                            if href:
                                url = ScraperUtils.normalize_url("https://iran-tejarat.com", href)
                            
                            title_el = link_el.find_element(By.TAG_NAME, "h2")
                            title = title_el.text.strip()
                        except: pass

                        # بررسی تکراری بودن
                        if DatabaseHandler.is_duplicate("irantejarat", url):
                            continue

                        # 2. استخراج شماره تماس (GlobalTelColor)
                        phone = "Hidden"
                        try:
                            # طبق HTML شما: <div class="GlobalTelColor">0912...</div>
                            tel_el = box.find_element(By.CLASS_NAME, "GlobalTelColor")
                            raw_tel = tel_el.text.strip()
                            # استخراج تمیز شماره‌ها
                            extracted = ScraperUtils.extract_phones_aggressive(raw_tel)
                            if extracted:
                                phone = " | ".join(extracted)
                        except: pass

                        # 3. استخراج شهر و نام (TextGray PrintCity)
                        location = "نامشخص" 
                        city = "نامشخص"     
                        try:
                            # طبق HTML شما: <span class="TextGray PrintCity">تهران , آسایش ...</span>
                            # سلکتور ترکیبی برای اطمینان
                            info_el = box.find_element(By.CSS_SELECTOR, ".PrintCity")
                            info_text = info_el.text.strip()
                            
                            if "," in info_text:
                                parts = info_text.split(",")
                                if len(parts) >= 1: city = parts[0].strip()
                                if len(parts) >= 2: location = parts[1].strip()
                            else:
                                city = info_text
                        except: pass

                        # ذخیره
                        if phone != "Hidden":
                            record = {
                                "title": title,
                                "phone": phone,
                                "location": location,
                                "email": "نامشخص",
                                "website": "نامشخص",
                                "address": city,
                                "category": keyword,
                                "url": url,
                                "keyword": keyword # Added Keyword
                            }
                            
                            success, msg = DatabaseHandler.save_record("irantejarat", record)
                            if success:
                                self.log(f"✅ دریافت شد: {phone} ({city})", "success")
                                new_count += 1
                    except Exception as e:
                        # خطا در پردازش یک باکس نباید کل لوپ را قطع کند
                        pass
                
                self.log(f"تعداد {new_count} رکورد جدید ذخیره شد.", "success")
                ScraperUtils.human_scroll(self.driver)
                time.sleep(random.uniform(2, 4))

            self.log("✅ عملیات پایان یافت.", "success")

        except Exception as e:
            self.log(f"❌ خطای کلی: {e}", "error")
        finally:
            if self.driver: 
                self.driver.quit()
                self.driver = None
            self.btn_start.configure(state="normal")

# =================================================================
#                  MODULE 7: UNIVERSAL SOCIAL BOT (UPDATED)
# =================================================================
class SmartChatBot:
    SELECTORS = {
        "WhatsApp": {
            "input": "div[contenteditable='true'][data-tab='10'], footer div[contenteditable='true']", 
            "send": "button[aria-label='Send'], span[data-icon='send']",
            "attach_btn": "span[data-icon='plus-rounded'], div[title='Attach'], span[data-icon='plus'], span[data-icon='clip']", 
            "file_input": "input[type='file']",
            "chat_list": "#side, div[aria-label='Chat list']"
        },
        "Telegram": {
            "input": ".input-message-input, .composer_rich_textarea, div[contenteditable='true']", 
            "send": "button.send, .btn-send, button[title='Send Message']",
            "attach_btn": "button.btn-attach, button[title='Attach media']",
            "modal_caption": ".input-caption-input",
            "chat_list": ".chat-list, .sidebar-header",
        },
        "Eitaa": {"input": ".input-message-input, div[contenteditable='true']", "send": ".btn-send", "chat_list": "app-chat-list, input[placeholder*='جستجو'], .chat-list", "attach_btn": "button.btn-attach, [title*='پیوست']"}, 
        "Bale": {"input": "div[contenteditable='true'], textarea, #message-input", "send": ".send-button, button[title*='ارسال']", "chat_list": "#sidebar, .sidebar, .chat-list, input[placeholder*='جستجو']", "attach_btn": "button.attach-button, [title*='ارسال فایل']"}, 
        "Rubika": {"input": "div[contenteditable='true']", "send": "div[class*='send']", "chat_list": ".chat-list, input[placeholder*='جستجو']"} 
    }
    
    URLS = {
        "WhatsApp": "https://web.whatsapp.com", 
        "Telegram": "https://web.telegram.org/k/",
        "Eitaa": "https://web.eitaa.com", 
        "Bale": "https://web.bale.ai", 
        "Rubika": "https://web.rubika.ir"
    }

    def __init__(self, platform, log_callback):
        self.platform = platform
        self.log = log_callback
        self.driver = None
        self.stop_signal = False
        self.selectors = self.SELECTORS.get(platform, self.SELECTORS["WhatsApp"])

    def start(self):
        self.driver = ScraperUtils.get_driver(headless=False)
        if self.driver:
            try:
                if self.platform == "Rubika":
                    self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"})
            except: pass
            try:
                self.log(f"⏳ در حال باز کردن {self.platform}...", "info")
                self.driver.get(self.URLS.get(self.platform, "about:blank"))
            except Exception as e: self.log(f"⚠️ خطا: {e}", "warning")
            return True
        return False

    def is_logged_in(self):
        try: return len(self.driver.find_elements(By.CSS_SELECTOR, self.selectors.get("chat_list", "body"))) > 0
        except: return False

    def wait_for_login(self, timeout=120):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.stop_signal: return False
            if self.is_logged_in(): return True
            time.sleep(1)
        return False

    def stop(self):
        self.stop_signal = True
        if self.driver:
            try: self.driver.quit()
            except: pass

    def send_to_number(self, phone, message, media_file=None):
        try:
            phone = ScraperUtils.to_english_digits(phone)
            clean_phone = re.sub(r'[^0-9]', '', phone)[-10:]

            if self.platform == "WhatsApp":
                url = f"https://web.whatsapp.com/send?phone=98{clean_phone}"
                self.driver.get(url)
                
                try: 
                    # انتظار هوشمندانه برای لود چت (وجود باکس متن یا دکمه‌های اصلی)
                    WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selectors["input"] + ", span[data-icon='send'], span[data-icon='plus-rounded']")))
                except: return False, "چت باز نشد یا شماره نامعتبر است"
                
                time.sleep(2) # مکث برای اطمینان از لود کامل رویدادها
                
                # --- بخش ارسال قطعی مدیا در واتس‌اپ ---
                if media_file and os.path.exists(media_file):
                    try:
                        # ۱. کلیک دقیق روی آیکون جدید واتس‌اپ (plus-rounded) برای باز شدن باکس منو
                        try:
                            attach_btn = WebDriverWait(self.driver, 10).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, self.selectors["attach_btn"]))
                            )
                            attach_btn.click()
                            time.sleep(1.5) # صبر برای باز شدن انیمیشن منوی "عکس‌ها و ویدئوها"
                        except Exception as e: 
                            print(f"Attach Button Error: {e}")
                            pass
                            
                        # ۲. پیدا کردن ورودی مخفی مختص "Photos and videos"
                        file_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
                        target_input = None
                        
                        # در بین input ها، آن موردی که تصاویر/ویدیو را می‌پذیرد پیدا می‌کنیم
                        for inp in file_inputs:
                            accept_attr = str(inp.get_attribute("accept")).lower()
                            if "image" in accept_attr or "video" in accept_attr:
                                target_input = inp; break
                        
                        if not target_input and file_inputs: 
                            target_input = file_inputs[0]
                        
                        if target_input:
                            # ۳. اتچ کردن فایل (این کار معادل کلیک روی گزینه Photos and Videos و انتخاب فایل است)
                            target_input.send_keys(os.path.abspath(media_file))
                            
                            # ۴. انتظار قطعی برای باز شدن پاپ‌آپ/مودال پیش‌نمایش عکس
                            wait = WebDriverWait(self.driver, 20)
                            caption_box = wait.until(EC.presence_of_element_located((
                                By.CSS_SELECTOR, 
                                "div[aria-placeholder*='caption'], div[aria-label*='Add a caption'], div[aria-label*='caption'], div[data-tab='10']"
                            )))
                            
                            time.sleep(1.5) # زمان برای لود کامل انیمیشن مودال
                            
                            # ۵. درج توضیحات در مودال با کلیک و پیست امن
                            caption_box.click()
                            time.sleep(0.5)
                            ScraperUtils.set_clipboard(message)
                            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                            time.sleep(1.5)
                            
                            # ۶. کلیک روی دکمه ارسال مخصوص مودال پیش‌نمایش
                            try:
                                send_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label='Send'], span[data-icon='send']")))
                                send_btn.click()
                            except:
                                ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                            
                            time.sleep(3)
                            return True, "مدیا و پیام ارسال شد"
                    except Exception as e:
                        print(f"WhatsApp Media Error: {e}")
                        # در صورت شکست، ادامه می‌دهد تا حداقل متن را بفرستد

                # --- ارسال پیام فقط متنی (واتس‌اپ) ---
                try:
                    boxes = self.driver.find_elements(By.CSS_SELECTOR, "div[contenteditable='true']")
                    visible_boxes = [b for b in boxes if b.is_displayed()]
                    if visible_boxes:
                        chat_box = visible_boxes[-1] # باکس چت اصلی معمولا آخرین باکس قابل مشاهده است
                        chat_box.click()
                        time.sleep(0.5)
                        ScraperUtils.set_clipboard(message)
                        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                        time.sleep(1)
                        
                        # زدن اینتر یا کلیک روی دکمه ارسال
                        send_btns = self.driver.find_elements(By.CSS_SELECTOR, "button[aria-label='Send'], span[data-icon='send']")
                        visible_btns = [b for b in send_btns if b.is_displayed()]
                        if visible_btns:
                            visible_btns[-1].click()
                        else:
                            ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                        
                        time.sleep(1.5)
                        return True, "ارسال شد"
                    else:
                        return False, "باکس پیام پیدا نشد"
                except Exception as e:
                    return False, f"خطا در ارسال متن: {str(e)[:30]}"

            elif self.platform == "Telegram":
                # حل مشکل URL تلگرام: در نسخه K از رزولور داخلی استفاده می‌شود
                tg_url = f"https://web.telegram.org/k/#?tgaddr=tg%3A%2F%2Fresolve%3Fphone%3D98{clean_phone}"
                self.driver.get(tg_url)
                time.sleep(5)
                
                try:
                    # تلگرام معمولا یک پاپ‌آپ باز می‌کند که باید روی Send Message کلیک کنیم
                    popups = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Send Message') or contains(text(), 'ارسال پیام')]")
                    if popups: 
                        popups[0].click()
                        time.sleep(2)
                    WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, self.selectors["input"])))
                except: 
                    if not self.driver.find_elements(By.CSS_SELECTOR, self.selectors["input"]):
                        return False, "چت باز نشد (شاید شماره در تلگرام نیست)"
                
                # --- بخش ارسال قطعی مدیا در تلگرام Web K ---
                if media_file and os.path.exists(media_file):
                    try:
                        # ۱. پیدا کردن input مخفی (تلگرام معمولا input را همیشه در DOM دارد)
                        file_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
                        if not file_inputs:
                            try:
                                attach_btns = self.driver.find_elements(By.CSS_SELECTOR, "button.btn-icon.attach-file, button.btn-attach, button[title='Attach media']")
                                if attach_btns: 
                                    attach_btns[0].click()
                                    time.sleep(1.5)
                            except: pass
                            file_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
                            
                        if file_inputs:
                            # ۲. تزریق فایل
                            file_inputs[0].send_keys(os.path.abspath(media_file))
                            
                            # ۳. انتظار برای پاپ‌آپ پیش‌نمایش در تلگرام
                            wait = WebDriverWait(self.driver, 20)
                            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-container, .modal-dialog")))
                            time.sleep(1.5) # زمان برای رندر شدن مودال
                            
                            # ۴. درج متن کپشن در پاپ‌آپ
                            try:
                                caption_boxes = self.driver.find_elements(By.CSS_SELECTOR, ".popup-container div[contenteditable='true'], .input-caption-input, .caption-input")
                                visible_caps = [b for b in caption_boxes if b.is_displayed()]
                                if visible_caps:
                                    cap_box = visible_caps[-1]
                                    cap_box.click()
                                    time.sleep(0.5)
                                    ScraperUtils.set_clipboard(message)
                                    ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                                    time.sleep(1.5)
                                else:
                                    # فال بک: تایپ مستقیم در پاپ‌آپ (اگر اتوماتیک فوکوس بود)
                                    ScraperUtils.set_clipboard(message)
                                    ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                                    time.sleep(1.5)
                            except: pass
                            
                            # ۵. کلیک روی دکمه ارسال پاپ‌آپ
                            try:
                                send_btns = self.driver.find_elements(By.CSS_SELECTOR, ".popup-container button.send, button.btn-primary.btn-color-primary, button[title='Send']")
                                visible_btns = [b for b in send_btns if b.is_displayed()]
                                if visible_btns: 
                                    visible_btns[-1].click()
                                else: 
                                    ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                            except:
                                ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                            
                            time.sleep(3)
                            return True, "مدیا و پیام ارسال شد"
                    except Exception as e:
                        print(f"Telegram Media Error: {e}")

                # --- ارسال پیام فقط متنی (تلگرام) ---
                try:
                    boxes = self.driver.find_elements(By.CSS_SELECTOR, "div[contenteditable='true']")
                    visible_boxes = [b for b in boxes if b.is_displayed()]
                    if visible_boxes:
                        chat_box = visible_boxes[-1]
                        chat_box.click()
                        time.sleep(0.5)
                        ScraperUtils.set_clipboard(message)
                        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                        time.sleep(1)
                        
                        send_btns = self.driver.find_elements(By.CSS_SELECTOR, "button.send, .btn-send, button[title='Send Message']")
                        visible_btns = [b for b in send_btns if b.is_displayed()]
                        if visible_btns:
                            visible_btns[-1].click()
                        else:
                            ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                        
                        time.sleep(1.5)
                        return True, "ارسال شد"
                    else:
                        return False, "باکس پیام پیدا نشد"
                except Exception as e:
                    return False, f"خطا در ارسال متن: {str(e)[:30]}"
                
            # --- B. لاجیک اختصاصی ایتا ---
            elif self.platform == "Eitaa":
                try:
                    temp_name = f"User_{clean_phone[-4:]}"
                    
                    try:
                        menu_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "new-menu")))
                        menu_btn.click()
                    except:
                        try:
                            self.driver.find_element(By.CSS_SELECTOR, ".btn-menu-toggle, .tgico-newchat_filled").click()
                        except: pass
                    
                    time.sleep(1)
                    try:
                        new_pv_btn = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".tgico-newprivate, .btn-menu-item.tgico-newprivate")))
                        new_pv_btn.click()
                    except: return False, "❌ گزینه پیام جدید یافت نشد"

                    time.sleep(1.5)
                    try:
                        add_contact_btn = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.tgico-add, .btn-circle.tgico-add")))
                        add_contact_btn.click()
                    except: return False, "دکمه افزودن مخاطب پیدا نشد"
                    
                    time.sleep(1)
                    try:
                        name_field = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".name-fields .input-field:nth-child(1) .input-field-input")))
                        name_field.send_keys(temp_name)
                    except:
                        inputs = self.driver.find_elements(By.CSS_SELECTOR, ".input-field-input")
                        if inputs: inputs[0].send_keys(temp_name)

                    try:
                        phone_field = self.driver.find_element(By.CSS_SELECTOR, ".input-field-phone .input-field-input")
                        phone_field.send_keys(Keys.CONTROL + "a")
                        phone_field.send_keys(Keys.DELETE)
                        if clean_phone.startswith("0"): final_phone = "+98" + clean_phone[1:]
                        elif clean_phone.startswith("98"): final_phone = "+" + clean_phone
                        else: final_phone = clean_phone
                        phone_field.send_keys(final_phone)
                    except Exception as e: return False, f"خطا در شماره: {e}"
                    
                    time.sleep(1)
                    try:
                        submit_btn = self.driver.find_element(By.CSS_SELECTOR, ".popup-header button.btn-primary")
                        if "disabled" in submit_btn.get_attribute("class"): time.sleep(1)
                        submit_btn.click()
                    except: return False, "دکمه ثبت پیدا نشد"
                    
                    time.sleep(3.5)
                    try:
                        error_toast = self.driver.find_elements(By.CLASS_NAME, "toast")
                        if error_toast:
                            txt = error_toast[0].text
                            if "not registered" in txt or "یافت نشد" in txt:
                                ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                                return False, "❌ شماره عضو ایتا نیست"
                    except: pass

                    try:
                        if self.driver.find_elements(By.CSS_SELECTOR, ".popup-container"):
                             ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                    except: pass

                    for _ in range(2):
                        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                        time.sleep(0.3)

                    try:
                        search_container = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, "main-search")))
                        search_input = search_container.find_element(By.TAG_NAME, "input")
                        search_input.click()
                        search_input.send_keys(Keys.CONTROL + "a")
                        search_input.send_keys(Keys.DELETE)
                        search_input.send_keys(temp_name)
                        time.sleep(4.0) 
                        
                        chat_opened = False
                        try:
                            target_xpath = f"//div[contains(@class, 'search-group-contacts')]//li[contains(@class, 'chatlist-chat') and .//span[contains(text(), '{temp_name}')]]"
                            target_el = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, target_xpath)))
                            target_el.click()
                            chat_opened = True
                        except:
                            search_input.send_keys(Keys.ENTER)
                            chat_opened = True

                        if chat_opened:
                            WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.selectors["input"])))
                            time.sleep(1) 
                            
                            # --- بخش ارسال مدیا ایتا ---
                            media_sent = False
                            if media_file and os.path.exists(media_file):
                                try:
                                    file_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
                                    if not file_inputs:
                                        attach_btns = self.driver.find_elements(By.CSS_SELECTOR, self.selectors.get("attach_btn", ".btn-attach, .attach-button"))
                                        if attach_btns:
                                            attach_btns[0].click()
                                            time.sleep(1)
                                            file_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
                                            
                                    if file_inputs:
                                        file_inputs[0].send_keys(os.path.abspath(media_file))
                                        time.sleep(3.5) 
                                        
                                        try:
                                            caption_boxes = self.driver.find_elements(By.CSS_SELECTOR, "div[contenteditable='true']")
                                            visible_caps = [b for b in caption_boxes if b.is_displayed()]
                                            if visible_caps:
                                                cap_box = visible_caps[-1]
                                                cap_box.click()
                                                time.sleep(0.5)
                                                ScraperUtils.set_clipboard(message)
                                                ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                                                time.sleep(1.5)
                                        except: pass
                                        
                                        # ارسال اجباری با اینتر در ایتا
                                        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                                        time.sleep(2.5)
                                        media_sent = True
                                except Exception as e:
                                    print(f"Media Error: {e}")

                            if not media_sent:
                                boxes = self.driver.find_elements(By.CSS_SELECTOR, "div[contenteditable='true']")
                                visible_boxes = [b for b in boxes if b.is_displayed()]
                                if visible_boxes:
                                    chat_box = visible_boxes[-1]
                                    chat_box.click()
                                    ScraperUtils.set_clipboard(message)
                                    ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                                    time.sleep(1)
                                    ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                                    time.sleep(1.5)
                                else:
                                    return False, "باکس پیام پیدا نشد"
                                    
                            ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                            return True, "ارسال شد"
                        else: return False, "چت باز نشد"

                    except Exception as e: return False, f"خطا جستجو: {str(e)[:50]}"

                except Exception as e:
                    try: ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                    except: pass
                    return False, f"خطا ایتا: {str(e)[:50]}"

            # --- C. Bale (با اصلاحات اساسی برای ارسال مدیا) ---
            elif self.platform == "Bale":
                try:
                    temp_name = f"User_{clean_phone[-4:]}"
                    
                    self.driver.get("https://web.bale.ai/contacts")
                    time.sleep(3.5)
                    
                    try:
                        add_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'B0w5tA') and contains(text(), 'افزودن مخاطب')]")))
                        add_btn.click()
                    except:
                        try:
                            self.driver.find_element(By.CSS_SELECTOR, "div[title='افزودن مخاطب']").click()
                        except: return False, "دکمه افزودن مخاطب پیدا نشد"
                    
                    time.sleep(1.5)
                    p_num = clean_phone
                    if p_num.startswith("98"): p_num = p_num[2:]
                    if p_num.startswith("+98"): p_num = p_num[3:]
                    if p_num.startswith("0"): p_num = p_num[1:]
                    
                    try:
                        phone_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='شماره همراه']")))
                        phone_input.send_keys(Keys.CONTROL + "a")
                        phone_input.send_keys(Keys.DELETE)
                        phone_input.send_keys(p_num)
                    except: return False, "فیلد تلفن بله یافت نشد"
                    
                    try:
                        name_input = self.driver.find_element(By.CSS_SELECTOR, "input[data-testid='نام']")
                        name_input.send_keys(Keys.CONTROL + "a")
                        name_input.send_keys(Keys.DELETE)
                        name_input.send_keys(temp_name)
                    except: return False, "فیلد نام بله یافت نشد"
                    
                    time.sleep(1)
                    try:
                        submit_btn = self.driver.find_element(By.CSS_SELECTOR, "button[aria-label='افزودن']")
                        if not submit_btn.is_enabled(): return False, "دکمه افزودن غیرفعال است"
                        submit_btn.click()
                    except: return False, "دکمه ثبت مخاطب پیدا نشد"
                    
                    time.sleep(4.0) 
                    
                    try:
                        try:
                            search_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.kXxU2w, div.rFuAsr, svg[aria-label='Search-icon']")))
                            search_btn.click()
                            time.sleep(1)
                        except: pass

                        search_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder*='جستجو'], input[type='search']")))
                        search_input.click()
                        search_input.send_keys(Keys.CONTROL + "a")
                        search_input.send_keys(Keys.DELETE)
                        search_input.send_keys(temp_name)
                        time.sleep(4.0) 
                        
                        chat_opened = False
                        
                        if not chat_opened:
                            try:
                                target_xpath = f"//div[contains(@class, 'oUKPfP') and text()='{temp_name}']"
                                result_el = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, target_xpath)))
                                result_el.click()
                                chat_opened = True
                            except: pass
                        
                        if not chat_opened:
                            try:
                                result_el = self.driver.find_element(By.CSS_SELECTOR, "div.qHFpb6, div[role='list'] > div")
                                result_el.click()
                                chat_opened = True
                            except: pass

                        if not chat_opened:
                            search_input.send_keys(Keys.ENTER)
                            chat_opened = True
                            
                        if not chat_opened: return False, "نتیجه جستجو پیدا نشد"
                        
                    except Exception as e: return False, f"خطا در جستجو/انتخاب: {str(e)[:50]}"
                    
                    try:
                        input_box = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[contenteditable='true'], textarea")))
                        input_box.click()
                        time.sleep(0.5)
                        
                        # --- بخش ارسال مدیا بله (حل مشکل کپشن و اینتر) ---
                        media_sent = False
                        if media_file and os.path.exists(media_file):
                            try:
                                file_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
                                if not file_inputs:
                                    attach_btns = self.driver.find_elements(By.CSS_SELECTOR, self.selectors.get("attach_btn", ".btn-attach, .attach-button"))
                                    if attach_btns:
                                        attach_btns[0].click()
                                        time.sleep(1)
                                        file_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
                                        
                                if file_inputs:
                                    file_inputs[0].send_keys(os.path.abspath(media_file))
                                    time.sleep(4.0) 
                                    
                                    try:
                                        # یافتن هوشمند باکس کپشن در بله
                                        modal_caps = self.driver.find_elements(By.CSS_SELECTOR, "div[role='dialog'] div[contenteditable='true'], .modal div[contenteditable='true'], textarea")
                                        visible_caps = [b for b in modal_caps if b.is_displayed()]
                                        if not visible_caps:
                                            visible_caps = [b for b in self.driver.find_elements(By.CSS_SELECTOR, "div[contenteditable='true']") if b.is_displayed()]
                                            
                                        if visible_caps:
                                            cap_box = visible_caps[-1]
                                            cap_box.click()
                                            time.sleep(0.5)
                                            ScraperUtils.set_clipboard(message)
                                            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                                            time.sleep(1.5)
                                        else:
                                            ScraperUtils.set_clipboard(message)
                                            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                                            time.sleep(1.5)
                                    except: pass
                                    
                                    # استفاده از اینتر برای تضمین ارسال مدیا در بله
                                    try:
                                        ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                                        time.sleep(0.5)
                                        
                                        # فال‌بک کلیک (اگر با اینتر نرفت)
                                        send_btns = self.driver.find_elements(By.CSS_SELECTOR, "button.send, .btn-primary, button[title*='ارسال']")
                                        visible_send = [b for b in send_btns if b.is_displayed()]
                                        if visible_send: 
                                            visible_send[-1].click()
                                    except: pass
                                    
                                    time.sleep(2.5)
                                    media_sent = True
                            except Exception as e:
                                print(f"Media Error: {e}")

                        # --- ارسال پیام فقط متنی (اگر مدیا نبود) ---
                        if not media_sent:
                            boxes = self.driver.find_elements(By.CSS_SELECTOR, "div[contenteditable='true']")
                            visible_boxes = [b for b in boxes if b.is_displayed()]
                            if visible_boxes:
                                chat_box = visible_boxes[-1]
                                chat_box.click()
                                ScraperUtils.set_clipboard(message)
                                ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                                time.sleep(1)
                                ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                                time.sleep(1.5)
                            else: return False, "باکس پیام پیدا نشد"
                        
                        return True, "ارسال شد"
                        
                    except TimeoutException: return False, "کادر پیام باز نشد (تایم‌اوت)"

                except Exception as e: return False, f"خطا بله: {str(e)[:50]}"

            # --- D. Rubika ---
            elif self.platform == "Rubika":
                try:
                    temp_name = f"User_{clean_phone[-4:]}"
                    
                    for _ in range(2):
                        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                        time.sleep(0.3)

                    try:
                        pencil_btn = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-menu-toggle, .rbico-pencil, .btn-float")))
                        pencil_btn.click()
                    except:
                        try:
                            self.driver.find_element(By.XPATH, "//div[contains(@class, 'float')]").click()
                        except: return False, "دکمه مداد (شروع پیام) یافت نشد"

                    time.sleep(1)
                    try:
                        new_msg_btn = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rbico-newprivate, .btn-menu-item.rbico-newprivate")))
                        new_msg_btn.click()
                    except: return False, "گزینه پیام جدید یافت نشد"

                    time.sleep(1.5)
                    try:
                        add_contact_btn = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".rbico-add, .btn-circle.rbico-add")))
                        add_contact_btn.click()
                    except: return False, "دکمه افزودن مخاطب (+) یافت نشد"
                    
                    time.sleep(1)
                    try:
                        fname_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.NAME, "first_name")))
                        fname_input.clear()
                        fname_input.send_keys(temp_name)
                        try:
                            lname_input = self.driver.find_element(By.NAME, "last_name")
                            lname_input.clear()
                            lname_input.send_keys(".")
                        except: pass

                        phone_input = self.driver.find_element(By.NAME, "phone")
                        phone_input.clear()
                        p_num = clean_phone
                        if p_num.startswith("0"): p_num = "+98" + p_num[1:]
                        elif p_num.startswith("98"): p_num = "+" + p_num
                        elif not p_num.startswith("+"): p_num = "+98" + p_num
                        phone_input.send_keys(p_num)
                    except: return False, "فیلدهای فرم مخاطب پیدا نشد"
                    
                    time.sleep(1)
                    try:
                        submit_btn = self.driver.find_element(By.CSS_SELECTOR, ".popup-header button.btn-primary")
                        submit_btn.click()
                    except: return False, "دکمه ثبت مخاطب پیدا نشد"
                    
                    time.sleep(4.0) 
                    try: ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                    except: pass
                    time.sleep(0.5)

                    try:
                        search_input = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input.input-search-input, input[placeholder*='جستجو']")))
                        search_input.click()
                        search_input.send_keys(Keys.CONTROL + "a")
                        search_input.send_keys(Keys.DELETE)
                        search_input.send_keys(temp_name)
                        time.sleep(3.5) 
                        
                        chat_opened = False
                        if not chat_opened:
                            try:
                                target_xpath = f"//div[contains(@class, 'search-group-contacts')]//li[.//span[contains(text(), '{temp_name}')]]"
                                target_el = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, target_xpath)))
                                target_el.click()
                                chat_opened = True
                            except: pass
                        
                        if not chat_opened:
                            try:
                                target_xpath = f"//div[contains(text(), '{temp_name}')]"
                                target_el = self.driver.find_element(By.XPATH, target_xpath)
                                target_el.click()
                                chat_opened = True
                            except: pass

                        if not chat_opened:
                            search_input.send_keys(Keys.ENTER)
                            chat_opened = True
                        
                        if not chat_opened: return False, "چت باز نشد (مخاطب یافت نشد)"

                    except Exception as e: return False, f"خطا در جستجو/باز کردن چت: {str(e)[:30]}"

                    try:
                        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.selectors["input"])))
                        time.sleep(0.5)
                        
                        # --- بخش ارسال مدیا روبیکا ---
                        media_sent = False
                        if media_file and os.path.exists(media_file):
                            try:
                                file_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
                                if not file_inputs:
                                    attach_btns = self.driver.find_elements(By.CSS_SELECTOR, self.selectors.get("attach_btn", ".btn-attach, .attach-button"))
                                    if attach_btns:
                                        attach_btns[0].click()
                                        time.sleep(1)
                                        file_inputs = self.driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
                                        
                                if file_inputs:
                                    file_inputs[0].send_keys(os.path.abspath(media_file))
                                    time.sleep(4.0) 
                                    
                                    try:
                                        caption_boxes = self.driver.find_elements(By.CSS_SELECTOR, "div[contenteditable='true']")
                                        visible_caps = [b for b in caption_boxes if b.is_displayed()]
                                        if visible_caps:
                                            cap_box = visible_caps[-1]
                                            cap_box.click()
                                            time.sleep(0.5)
                                            ScraperUtils.set_clipboard(message)
                                            ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                                            time.sleep(1.5)
                                    except: pass
                                    
                                    # استفاده از اینتر در روبیکا
                                    ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                                    time.sleep(2.5)
                                    media_sent = True
                            except Exception as e:
                                print(f"Media Error: {e}")

                        if not media_sent:
                            boxes = self.driver.find_elements(By.CSS_SELECTOR, "div[contenteditable='true']")
                            visible_boxes = [b for b in boxes if b.is_displayed()]
                            if visible_boxes:
                                chat_box = visible_boxes[-1]
                                chat_box.click()
                                ScraperUtils.set_clipboard(message)
                                ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                                time.sleep(1)
                                ActionChains(self.driver).send_keys(Keys.ENTER).perform()
                                time.sleep(1.5)
                            else: return False, "باکس پیام پیدا نشد"
                        
                        time.sleep(2.0)
                        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                        return True, "ارسال شد"
                    except TimeoutException: return False, "کادر پیام باز نشد (تایم‌اوت)"

                except Exception as e: 
                    try: ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
                    except: pass
                    return False, f"خطا روبیکا: {str(e)[:50]}"

            else:
                return False, "ارسال در این پلتفرم در این نسخه محدود است."
        except Exception as e: return False, str(e)

# =================================================================
#                  MODULE: CRM FRAME (PREMIUM EDITION)
# =================================================================
class CRMFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=THEME["bg_root"])
        self.TABLE_MAP = {
            "اینستاگرام": "instagram", "دیوار": "divar", "شیپور": "sheypoor", 
            "ترب": "torob", "نشان": "neshan", "نیازروز": "niazrooz", "گوگل مپس": "maps", 
            "اول": "avval", "ایران تجارت": "irantejarat", "باسکول": "buskool",
            "شماره‌های من": "accounts"
        }
        self.bot = None
        self.current_prod_img = None
        self.current_prod_vid = None
        self.excel_numbers = []     
        self.excel_numbers_sms = [] 
        self.selected_phones = set() 
        self.configure_grid()
        self.style_treeview()
        self.setup_ui()

    def configure_grid(self):
        # تنظیم مجدد عرض: سایدبار ۵۰٪ عریض‌تر شد (وزن ۱۲ در برابر ۴) برای نمایش کامل در مانیتورهای ۱۰ اینچ
        self.grid_columnconfigure(0, weight=12) # پنل ابزار (چپ) - بسیار عریض
        self.grid_columnconfigure(1, weight=4)  # پنل دیتابیس (راست) - جمع‌وجور
        self.grid_rowconfigure(0, weight=1)

    def style_treeview(self):
        style = ttk.Style()
        style.theme_use("clam")
        
        # استایل مدرن جدول - فونت کوچک‌تر شده (10) برای نمایش کامل محتوا
        style.configure("Treeview", 
                        background=THEME["bg_card"], 
                        foreground="white", 
                        fieldbackground=THEME["bg_card"], 
                        rowheight=45, 
                        font=(APP_FONT, 10), # تغییر سایز فونت از 11 به 10
                        borderwidth=0)
        
        style.configure("Treeview.Heading", 
                        background=THEME["bg_input"], 
                        foreground=THEME["primary"], 
                        font=(APP_FONT, 11, "bold"), # هدر کمی بزرگتر و بولد
                        borderwidth=0,
                        relief="flat")
        
        style.map("Treeview", 
                  background=[("selected", THEME["primary_hover"])], 
                  foreground=[("selected", "black")])

    def setup_ui(self):
        # --- پنل سمت راست: بانک اطلاعاتی (Database) ---
        right_container = ctk.CTkFrame(self, fg_color=THEME["bg_card"], corner_radius=15, border_width=1, border_color=THEME["border"])
        right_container.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        # هدر دیتابیس
        db_header = ctk.CTkFrame(right_container, fg_color="transparent")
        db_header.pack(fill="x", padx=20, pady=15)
        ctk.CTkLabel(db_header, text="🗂️ بانک جامع مشتریان", font=(APP_FONT, 20, "bold"), text_color=THEME["primary"]).pack(side="right")
        ctk.CTkLabel(db_header, text="مدیریت داده‌های استخراج شده", font=(APP_FONT, 12), text_color="gray").pack(side="right", padx=10, pady=5)

        # تب‌های دیتابیس
        self.tabs_db = ctk.CTkTabview(right_container, fg_color="transparent", 
                                      text_color=THEME["text_main"], 
                                      segmented_button_fg_color=THEME["bg_input"], 
                                      segmented_button_selected_color=THEME["primary"], 
                                      segmented_button_unselected_color=THEME["bg_root"],
                                      corner_radius=10, height=40)
        self.tabs_db._segmented_button.configure(font=(APP_FONT, 12, "bold"))
        self.tabs_db.pack(fill="both", expand=True, padx=10, pady=(0, 10))
        
        for k in self.TABLE_MAP.keys(): 
            self.tabs_db.add(k)
            self.build_db_tab(k)

        # --- پنل سمت چپ: ابزارها (Tools - Premium Sidebar) ---
        left_container = ctk.CTkFrame(self, fg_color=THEME["bg_sidebar"], corner_radius=0)
        left_container.grid(row=0, column=0, sticky="nsew")
        left_container.pack_propagate(False)
        
        # هدر ابزارها
        tool_head = ctk.CTkFrame(left_container, fg_color="transparent")
        tool_head.pack(fill="x", padx=15, pady=20)
        ctk.CTkLabel(tool_head, text="🛠️ ابزارهای مارکتینگ", font=(APP_FONT, 22, "bold"), text_color="white").pack(anchor="center")

        # استفاده از اسکرول برای پنل ابزار جهت نمایش کامل در مانیتورهای کوچک
        self.tools_scroll = ctk.CTkScrollableFrame(left_container, fg_color="transparent")
        self.tools_scroll.pack(fill="both", expand=True, padx=5, pady=5)

        self.tabs_tools = ctk.CTkTabview(self.tools_scroll, fg_color="transparent", 
                                         segmented_button_fg_color=THEME["bg_input"], 
                                         segmented_button_selected_color=THEME["secondary"],
                                         text_color="white", height=800)
        self.tabs_tools._segmented_button.configure(font=(APP_FONT, 12, "bold"))
        self.tabs_tools.pack(fill="both", expand=True, padx=5, pady=(0, 10))
        
        # فراخوانی ستاپ تب‌ها
        self.setup_sms_tab()         
        self.setup_social_bulk_tab() 
        self.setup_products_tab()    
        self.setup_bot_tab()         

    def build_db_tab(self, name):
        t = self.tabs_db.tab(name)
        
        # نوار ابزار بالای جدول
        toolbar = ctk.CTkFrame(t, fg_color=THEME["bg_input"], height=45, corner_radius=8)
        toolbar.pack(fill="x", pady=(5, 10))
        
        # بخش فیلتر
        filter_frame = ctk.CTkFrame(toolbar, fg_color="transparent")
        filter_frame.pack(side="right", padx=5)
        
        # دکمه جستجو (تعریف اولیه)
        btn_search = ctk.CTkButton(filter_frame, text="🔍", width=40, height=28, 
                      font=(APP_FONT, 14), fg_color=THEME["primary"])
        btn_search.pack(side="right", padx=2)
        
        # ورودی جستجو
        ent_filter_kw = ctk.CTkEntry(filter_frame, width=140, height=30, font=(APP_FONT, 12), placeholder_text="جستجو...")
        ent_filter_kw.pack(side="right", padx=2)
        add_context_menu(ent_filter_kw) # افزودن منو به فیلتر جستجو

        # دکمه‌های عملیاتی (تعریف اولیه)
        btn_sms = ctk.CTkButton(toolbar, text="ارسال به پیامک", width=110, height=28,
                      font=(APP_FONT, 11, "bold"), fg_color=THEME["warning"], hover_color="#F57C00")
        btn_sms.pack(side="left", padx=5)

        lbl_count = ctk.CTkLabel(toolbar, text="تعداد: ۰", font=(APP_FONT, 12, "bold"), text_color=THEME["info"])
        lbl_count.pack(side="right", padx=15)
        
        btn_refresh = ctk.CTkButton(toolbar, text="🔄", width=30, height=28, 
                      font=(APP_FONT, 14), fg_color=THEME["secondary"])
        btn_refresh.pack(side="right", padx=5)

        # کانتینر جدول
        tree_container = ctk.CTkFrame(t, fg_color="transparent")
        tree_container.pack(fill="both", expand=True)

        vsb = ttk.Scrollbar(tree_container, orient="vertical")
        hsb = ttk.Scrollbar(tree_container, orient="horizontal")

        # تعریف ستون‌ها به ترتیب بصری راست به چپ (RTL Simulation)
        cols = ("col4", "col3", "col2", "col1", "row", "check")
        tree = ttk.Treeview(tree_container, columns=cols, show="headings", 
                            selectmode="extended", yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        
        vsb.config(command=tree.yview)
        hsb.config(command=tree.xview)
        
        vsb.pack(side="left", fill="y")
        hsb.pack(side="bottom", fill="x")
        tree.pack(side="right", fill="both", expand=True)
        
        # تنظیم هدرها (تراز راست)
        tree.heading("check", text="انتخاب"); tree.column("check", width=50, anchor="center", stretch=False)
        tree.heading("row", text="#"); tree.column("row", width=50, anchor="center", stretch=False)
        tree.heading("col1", text="عنوان / نام"); tree.column("col1", width=150, anchor="e") 
        tree.heading("col2", text="تلفن"); tree.column("col2", width=110, anchor="center")
        tree.heading("col3", text="توضیحات / آدرس"); tree.column("col3", width=200, anchor="e") 
        tree.heading("col4", text="کلیدواژه"); tree.column("col4", width=100, anchor="center")
        
        tree.bind('<ButtonRelease-1>', lambda event: self.on_table_click(event, tree))
        
        # اتصال عملکردها (بعد از ساخته شدن tree و ویجت‌ها)
        btn_search.configure(command=lambda: self.refresh_db_tab(tree, name, lbl_count, ent_filter_kw.get()))
        btn_refresh.configure(command=lambda: self.refresh_db_tab(tree, name, lbl_count, ent_filter_kw.get()))
        btn_sms.configure(command=lambda: self.send_to_selected("sms", tree))
        
        self.refresh_db_tab(tree, name, lbl_count)

    def refresh_db_tab(self, tree, name, lbl_widget, keyword_filter=None):
        # 1. پاکسازی جدول
        for i in tree.get_children(): tree.delete(i)
        
        # 2. دریافت نام انگلیسی جدول از روی نام فارسی تب
        db_table = self.TABLE_MAP.get(name)
        if not db_table: return

        # 3. دریافت داده‌ها
        rows = DatabaseHandler.fetch_crm_data(db_table, keyword_filter)
        
        # 4. نمایش تعداد
        lbl_widget.configure(text=f"تعداد: {len(rows):,}")
        
        # 5. پر کردن جدول
        for i, r in enumerate(rows):
            # r ساختاری شبیه به (c1, c2, c3, "", "", "", c4) دارد
            c1 = r[0] # Title
            c2 = r[1] # Phone
            c3 = r[2] # Desc
            c4 = r[6] # Keyword (Index 6)
            
            check_mark = "☐"
            
            # ترتیب نمایش در ستون‌های Treeview (باید با تعریف ستون‌ها در setup_ui هماهنگ باشد)
            # cols = ("col4", "col3", "col2", "col1", "row", "check")
            # col4=Keyword, col3=Desc, col2=Phone, col1=Title
            vals = (c4, c3, c2, c1, i+1, check_mark)
            
            tag = "even" if i % 2 == 0 else "odd"
            tree.insert("", "end", iid=i, values=vals, tags=(tag,))
            
        tree.tag_configure("even", background=THEME["table_row_even"])
        tree.tag_configure("odd", background=THEME["table_row_odd"])

    def on_table_click(self, event, tree):
        region = tree.identify_region(event.x, event.y)
        if region == "cell":
            col = tree.identify_column(event.x)
            # ستون چک باکس آخرین ستون تعریف شده است (#6)
            if col == "#6": 
                item_id = tree.identify_row(event.y)
                if item_id:
                    current_vals = tree.item(item_id, "values")
                    new_mark = "☑" if current_vals[5] == "☐" else "☐"
                    new_vals = list(current_vals)
                    new_vals[5] = new_mark
                    tree.item(item_id, values=new_vals)
                    
                    phone = current_vals[2] # ایندکس تلفن در تاپل vals
                    if new_mark == "☑": self.selected_phones.add(phone)
                    else: self.selected_phones.discard(phone)

    def send_to_selected(self, mode, tree):
        phones = []
        for child in tree.get_children():
            vals = tree.item(child, "values")
            if vals[5] == "☑": # ایندکس چک باکس
                p = vals[2]
                if p and p != "-" and p != "Hidden":
                    phones.append(p)
        
        if not phones:
            messagebox.showwarning("هشدار", "هیچ شماره‌ای انتخاب نشده است.")
            return
            
        phones_str = "\n".join(phones)
        if mode == "sms":
            self.tabs_tools.set("✉️ پیامک پرو")
            self.txt_sms_manual.delete("1.0", "end")
            self.txt_sms_manual.insert("end", phones_str)
            messagebox.showinfo("انتقال موفق", f"{len(phones)} شماره منتقل شد.")

    # =================================================================
    #  💎 PREMIUM SMS TAB DESIGN (WITH RANGE & AI FIXES) 💎
    # =================================================================
    def setup_sms_tab(self):
        t = self.tabs_tools.add("✉️ پیامک پرو")
        
        # --- کارت وضعیت حساب ---
        wallet_card = ctk.CTkFrame(t, fg_color=THEME["bg_card"], corner_radius=12, border_color=THEME["border"], border_width=1)
        wallet_card.pack(fill="x", padx=10, pady=(10, 5))
        
        bal_frame = ctk.CTkFrame(wallet_card, fg_color="transparent")
        bal_frame.pack(side="left", padx=15, pady=10)
        self.lbl_sms_balance = ctk.CTkLabel(bal_frame, text="موجودی: ...", font=(APP_FONT, 13, "bold"), text_color=THEME["success"])
        self.lbl_sms_balance.pack()
        ctk.CTkButton(wallet_card, text="شارژ +", width=60, height=25, fg_color=THEME["success"], text_color="black", command=self.open_wallet_recharge).pack(side="left", padx=5)
        
        ctk.CTkLabel(wallet_card, text="پنل پیامک هوشمند", font=(APP_FONT, 14, "bold"), text_color=THEME["sms_panel"]).pack(side="right", padx=15)
        self.update_sms_tab_balance()

        # --- بخش تنظیمات اکانت ---
        cred_frame = ctk.CTkFrame(t, fg_color="transparent")
        cred_frame.pack(fill="x", padx=10)
        
        # استفاده از مقادیر صحیح کانفیگ
        self.ent_sms_user = ctk.CTkEntry(cred_frame, placeholder_text="User", width=100)
        self.ent_sms_user.pack(side="left", padx=2)
        self.ent_sms_user.insert(0, SMS_CONFIG["username"])
        add_context_menu(self.ent_sms_user)
        
        self.ent_sms_pass = ctk.CTkEntry(cred_frame, placeholder_text="Pass", show="*", width=100)
        self.ent_sms_pass.pack(side="left", padx=2)
        self.ent_sms_pass.insert(0, SMS_CONFIG["password"])
        add_context_menu(self.ent_sms_pass)
        
        ctk.CTkLabel(cred_frame, text="خط: +989989000", font=("vazir", 10, "bold"), text_color="gray").pack(side="right", padx=10)

        # --- بخش هدف‌گیری (Targeting) ---
        target_card = ctk.CTkFrame(t, fg_color=THEME["bg_card"], corner_radius=12)
        target_card.pack(fill="x", padx=10, pady=10)
        ctk.CTkLabel(target_card, text="👥 گیرندگان", font=(APP_FONT, 12, "bold"), text_color=THEME["info"]).pack(anchor="e", padx=15, pady=5)

        # 1. دکمه اکسل
        excel_frame = ctk.CTkFrame(target_card, fg_color="transparent"); excel_frame.pack(fill="x", padx=10)
        self.lbl_sms_excel_stat = ctk.CTkLabel(excel_frame, text="", font=(APP_FONT, 10), text_color=THEME["success"])
        self.lbl_sms_excel_stat.pack(side="right", padx=5)
        ctk.CTkButton(excel_frame, text="📂 اکسل", width=80, height=25, command=self.load_excel_numbers_sms).pack(side="right")
        
        # 2. سوئیچ کل دیتابیس
        self.chk_all = ctk.CTkSwitch(target_card, text="کل لیست دیتابیس", font=(APP_FONT, 11), progress_color=THEME["primary"])
        self.chk_all.pack(anchor="e", padx=15, pady=5)

        # 3. انتخاب بازه‌ای (قابلیت جدید: انتقال به لیست)
        range_frame = ctk.CTkFrame(target_card, fg_color=THEME["bg_input"], corner_radius=8)
        range_frame.pack(fill="x", padx=10, pady=5)
        
        self.chk_range_sms = ctk.CTkSwitch(range_frame, text="ارسال مستقیم بازه", font=(APP_FONT, 11), progress_color=THEME["warning"])
        self.chk_range_sms.pack(side="right", padx=5, pady=5)
        
        self.ent_range_to_sms = ctk.CTkEntry(range_frame, width=50, placeholder_text="تا", justify="center")
        self.ent_range_to_sms.pack(side="right", padx=5, pady=5)
        add_context_menu(self.ent_range_to_sms)
        ctk.CTkLabel(range_frame, text="تا", font=(APP_FONT, 10)).pack(side="right")
        
        self.ent_range_from_sms = ctk.CTkEntry(range_frame, width=50, placeholder_text="از", justify="center")
        self.ent_range_from_sms.pack(side="right", padx=5, pady=5)
        add_context_menu(self.ent_range_from_sms)
        ctk.CTkLabel(range_frame, text="از ردیف", font=(APP_FONT, 10)).pack(side="right")

        # دکمه انتقال
        ctk.CTkButton(range_frame, text="⬇ انتقال به لیست دستی", width=110, height=24, 
                      fg_color=THEME["secondary"], text_color="black", font=(APP_FONT, 10, "bold"),
                      command=self.fetch_range_numbers).pack(side="left", padx=10)

        # 4. ورودی دستی
        ctk.CTkLabel(target_card, text="شماره دستی (قابل ویرایش):", font=(APP_FONT, 11), text_color="gray").pack(anchor="e", padx=15)
        self.txt_sms_manual = ctk.CTkTextbox(target_card, height=50, font=("vazir", 11), border_width=1, border_color=THEME["border"], fg_color=THEME["bg_input"])
        self.txt_sms_manual.pack(fill="x", padx=10, pady=(0, 10))
        add_context_menu(self.txt_sms_manual) # افزودن منو راست کلیک

        # --- بخش محتوا ---
        msg_frame = ctk.CTkFrame(t, fg_color="transparent")
        msg_frame.pack(fill="x", padx=10, pady=5)
        ctk.CTkButton(msg_frame, text="✨ تولید متن با هوش مصنوعی", fg_color="transparent", text_color=THEME["primary"], height=20, command=self.ai_sms).pack(anchor="w")
        self.txt_sms = ctk.CTkTextbox(msg_frame, height=80, font=(APP_FONT, 12), border_width=2, border_color=THEME["bg_input"])
        self.txt_sms.pack(fill="x", pady=2); self.txt_sms.tag_config("rtl", justify='right')
        self.txt_sms.bind('<KeyRelease>', self.update_sms_cost_label)
        add_context_menu(self.txt_sms) # افزودن منو راست کلیک
        
        self.lbl_cost = ctk.CTkLabel(t, text="هزینه: ۰", font=(APP_FONT, 10), text_color="gray"); self.lbl_cost.pack(anchor="e", padx=20)

        # دکمه ارسال
        self.btn_send_sms = ctk.CTkButton(t, text="🚀 ارسال پیامک", height=45, font=(APP_FONT, 14, "bold"), fg_color=THEME["sms_panel"], hover_color="#D84315", command=self.send_sms)
        self.btn_send_sms.pack(fill="x", padx=10, pady=20)

    def fetch_range_numbers(self):
        """انتقال شماره‌های بازه انتخابی به لیست دستی"""
        try:
            start = int(self.ent_range_from_sms.get())
            end = int(self.ent_range_to_sms.get())
        except ValueError:
            messagebox.showerror("خطا", "لطفاً شماره ردیف معتبر وارد کنید (عدد).")
            return

        active_tab = self.tabs_db.get()
        table = self.TABLE_MAP.get(active_tab)
        if not table:
            messagebox.showerror("خطا", "لطفا ابتدا یک جدول از دیتابیس را انتخاب کنید.")
            return

        all_phones = DatabaseHandler.fetch_phones(table)
        
        if not all_phones:
            messagebox.showerror("خطا", "جدول انتخابی خالی است یا شماره‌ای ندارد.")
            return

        if start < 1: start = 1
        if end > len(all_phones): end = len(all_phones)
        
        if start > end:
            messagebox.showerror("خطا", "شماره شروع نمی‌تواند بزرگتر از پایان باشد.")
            return

        # برش لیست (ایندکس پایتون از 0 شروع می‌شود)
        subset = all_phones[start-1:end]
        
        if not subset:
            messagebox.showwarning("هشدار", "شماره‌ای در این بازه یافت نشد.")
            return

        # اضافه کردن به تکست باکس
        current_text = self.txt_sms_manual.get("1.0", "end").strip()
        new_numbers_str = "\n".join(subset)
        
        final_text = ""
        if current_text:
            final_text = current_text + "\n" + new_numbers_str
        else:
            final_text = new_numbers_str
            
        self.txt_sms_manual.delete("1.0", "end")
        self.txt_sms_manual.insert("end", final_text)
        
        messagebox.showinfo("انتقال موفق", f"{len(subset)} شماره از ردیف {start} تا {end} به لیست اضافه شد.")

    def update_sms_cost_label(self, event=None):
        text = self.txt_sms.get("1.0", "end-1c").strip()
        length = len(text); count = 1 if length == 0 else (length // 60) + 1
        self.lbl_cost.configure(text=f"طول: {length} | پیامک: {count} | هزینه واحد: {count*200} تومان")

    def update_sms_tab_balance(self):
        try:
            bal = DatabaseHandler.get_wallet_balance()
            self.lbl_sms_balance.configure(text=f"موجودی: {int(bal):,} تومان")
        except: pass

    def open_wallet_recharge(self):
        try: self.winfo_toplevel().show_frame("wallet")
        except: pass

    def ai_sms(self): 
        self.txt_sms.delete("1.0", "end"); self.txt_sms.insert("end", "⏳ در حال تفکر...", "rtl")
        threading.Thread(target=self._ai_sms_thread, daemon=True).start()

    def _ai_sms_thread(self):
        """تولید متن با فال‌بک سریع در صورت خرابی AI"""
        text = ""
        # 1. تلاش برای استفاده از AI
        if AI_AVAILABLE:
            try:
                ctx = AIBrain.DATA
                prompt = f"متن پیامک تبلیغاتی کوتاه فارسی برای {ctx.get('business_name')} با تخفیف ویژه. (حداکثر 2 خط)"
                client = G4FClient()
                resp = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role":"user", "content":prompt}])
                text = resp.choices[0].message.content
                if "error" in text.lower(): text = "" # اگر خطا در متن بود
            except: pass
        
        # 2. استفاده از قالب آماده اگر AI کار نکرد
        if not text:
            import random
            templates = [
                "فروش ویژه فصل آغاز شد! 🎉\nتخفیف‌های استثنایی را از دست ندهید.\nاطلاعات بیشتر تماس با ما.",
                "دنبال کیفیت بالا هستید؟ 💎\nمحصولات جدید ما رسید. ارسال رایگان.\nلینک سفارش: ...",
                f"خبر خوب برای مشتریان {AIBrain.DATA.get('business_name', 'عزیز')} 📣\nتخفیف روی تمامی محصولات تا پایان هفته.",
            ]
            text = random.choice(templates)

        self.after(0, lambda: [self.txt_sms.delete("1.0", "end"), self.txt_sms.insert("end", text, "rtl"), self.update_sms_cost_label()])

    def send_sms(self):
        msg = self.txt_sms.get("1.0", "end-1c").strip()
        if not msg: messagebox.showerror("خطا", "متن پیامک خالی است."); return
        
        user = self.ent_sms_user.get(); pwd = self.ent_sms_pass.get()
        targets = []
        
        # 1. از دیتابیس (کل یا بازه)
        if self.chk_all.get() or self.chk_range_sms.get():
            active_tab = self.tabs_db.get()
            table = self.TABLE_MAP.get(active_tab)
            if table:
                all_phones = DatabaseHandler.fetch_phones(table)
                
                if self.chk_range_sms.get():
                    try:
                        start = int(self.ent_range_from_sms.get())
                        end = int(self.ent_range_to_sms.get())
                        if start < 1: start = 1
                        if end > len(all_phones): end = len(all_phones)
                        if start <= end:
                            targets.extend(all_phones[start-1:end])
                        else:
                            messagebox.showerror("خطا", "بازه نامعتبر است.")
                            return
                    except ValueError:
                        messagebox.showerror("خطا", "لطفاً شماره ردیف معتبر وارد کنید.")
                        return
                elif self.chk_all.get():
                    targets.extend(all_phones)

        # 2. اکسل
        if self.excel_numbers_sms: targets.extend(self.excel_numbers_sms)
        
        # 3. دستی
        manual_txt = self.txt_sms_manual.get("1.0", "end").strip()
        if manual_txt:
            targets.extend([ScraperUtils.to_english_digits(m.strip()) for m in re.split(r'[,\n\r]+', manual_txt) if m.strip()])
            
        targets = ScraperUtils.uniq(targets)
        if not targets: messagebox.showerror("خطا", "گیرنده‌ای یافت نشد."); return

        # محاسبه هزینه
        import math; msg_len = len(msg); sms_count = math.ceil(msg_len / 60) if msg_len > 0 else 1
        total_cost = len(targets) * sms_count * 200
        bal = DatabaseHandler.get_wallet_balance()
        
        if bal < total_cost: messagebox.showerror("موجودی ناکافی", f"هزینه: {total_cost:,}\nموجودی: {bal:,}"); return

        if messagebox.askyesno("تایید", f"ارسال به {len(targets)} نفر؟\nهزینه: {total_cost:,} تومان"):
            # شروع ترد ارسال پیامک
            threading.Thread(target=self._sms_worker, args=(targets, msg, user, pwd, sms_count * 200)).start()

    def _sms_worker(self, targets, msg, user, pwd, cost_per_person):
        """
        ارسال پیامک با پایداری بالا (بدون استفاده از Session برای جلوگیری از خطای Prematurely)
        """
        domain = SMS_CONFIG["DOMAIN"]
        raw_sender = SMS_CONFIG["line_options"][0] if SMS_CONFIG["line_options"] else "+989989000"
        
        # اصلاح فرمت شماره فرستنده
        sender = raw_sender.strip()
        if sender.isdigit():
            if sender.startswith("0"): sender = "+98" + sender[1:]
            elif sender.startswith("98"): sender = "+" + sender
            else: sender = "+98" + sender
            
        success = 0
        failed = 0
        last_error_details = ""
        
        # هدرهای پایه با بستن کانکشن برای جلوگیری از خطای سرور
        base_headers = {
            'Content-Type': 'text/xml; charset=utf-8',
            'Connection': 'close',  # حیاتی برای رفع خطای Response ended prematurely
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        url = f"http://{domain}/webservice/send.php"

        # 1. استعلام اعتبار (اختیاری - جهت تست اتصال)
        try:
            cred_body = f"""<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://{domain}/webservice/send.php" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body><ns1:GetCredit><Username xsi:type="xsd:string">{user}</Username><Password xsi:type="xsd:string">{pwd}</Password></ns1:GetCredit></SOAP-ENV:Body></SOAP-ENV:Envelope>"""
            h_cred = base_headers.copy()
            h_cred['SOAPAction'] = f"http://{domain}/webservice/send.php/GetCredit"
            
            # استفاده از requests.post مستقیم (بدون سشن)
            requests.post(url, data=cred_body.encode('utf-8'), headers=h_cred, timeout=10, proxies={"http": None, "https": None})
        except: pass
            
        # 2. حلقه ارسال
        for p in targets:
            try:
                # استانداردسازی شماره گیرنده
                clean_p = ScraperUtils.to_english_digits(str(p))
                clean_p = re.sub(r'[^0-9]', '', clean_p)
                if clean_p.startswith("0"): clean_p = "+98" + clean_p[1:]
                elif clean_p.startswith("98"): clean_p = "+" + clean_p
                elif not clean_p.startswith("+"): clean_p = "+98" + clean_p
                
                soap_body = f"""<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://{domain}/webservice/send.php" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body><ns1:SendSMS><fromNum xsi:type="xsd:string">{sender}</fromNum><toNum SOAP-ENC:arrayType="xsd:string[1]" xsi:type="SOAP-ENC:Array"><item xsi:type="xsd:string">{clean_p}</item></toNum><Content xsi:type="xsd:string">{msg}</Content><Type xsi:type="xsd:string">0</Type><Username xsi:type="xsd:string">{user}</Username><Password xsi:type="xsd:string">{pwd}</Password></ns1:SendSMS></SOAP-ENV:Body></SOAP-ENV:Envelope>"""
                
                h_send = base_headers.copy()
                h_send['SOAPAction'] = f"http://{domain}/webservice/send.php/SendSMS"
                
                # ارسال درخواست (تایم‌اوت بیشتر و بدون پراکسی)
                resp = requests.post(url, data=soap_body.encode('utf-8'), headers=h_send, timeout=25, proxies={"http": None, "https": None})
                
                resp_content = resp.text
                
                # بررسی موفقیت
                # کدهای موفق معمولاً طولانی هستند (کد پیگیری) یا خطای Fault ندارند
                is_fault = "Fault" in resp_content or "Exception" in resp_content
                is_html_error = "<html" in resp_content
                
                if resp.status_code == 200 and not is_fault and not is_html_error and len(resp_content) > 5:
                    success += 1
                    print(f"SMS OK: {clean_p}")
                else:
                    failed += 1
                    err = self._extract_soap_error(resp_content)
                    if not err: err = f"Status: {resp.status_code}"
                    last_error_details = err
                    print(f"SMS Failed: {clean_p} -> {err}")
                    
            except Exception as e: 
                failed += 1
                last_error_details = str(e)
                print(f"SMS Exception: {e}")
        
        # نمایش گزارش نهایی در ترد اصلی
        self.after(0, lambda: self._show_final_report(success, failed, cost_per_person, last_error_details))

    def _extract_soap_error(self, text):
        try:
            if "faultstring" in text: return text.split("<faultstring>")[1].split("</faultstring>")[0]
            match = re.search(r'<item[^>]*>([^<]+)</item>', text)
            if match: return match.group(1)
            # تلاش برای یافتن متن خطا در تگ return
            match_ret = re.search(r'<return[^>]*>([^<]+)</return>', text)
            if match_ret: return match_ret.group(1)
            return ""
        except: return ""

    def _show_final_report(self, success, failed, cost, error_msg):
        self.btn_send_sms.configure(state="normal", text="🚀 ارسال پیامک", fg_color=THEME["sms_panel"])
        if success > 0:
            total_deduct = success * cost
            DatabaseHandler.add_wallet_transaction("withdraw", total_deduct, f"ارسال پیامک ({success} نفر)")
            self.update_sms_tab_balance()
            msg = f"✅ ارسال موفق: {success} عدد\n❌ ناموفق: {failed} عدد"
            if failed > 0: msg += f"\n\n⚠️ نمونه خطا: {error_msg}"
            messagebox.showinfo("گزارش ارسال", msg)
        else:
            translated_error = error_msg
            if "emkan pazir nist" in str(error_msg).lower(): translated_error = "ارسال از خط اختصاصی مجاز نیست."
            elif "credit" in str(error_msg).lower(): translated_error = "اعتبار ناکافی."
            elif "prematurely" in str(error_msg).lower(): translated_error = "قطع ارتباط با سرور (Prematurely)."
            
            messagebox.showerror("خطا در ارسال", f"❌ پیامک ارسال نشد.\n\n🔍 علت:\n{translated_error}")

    def _sms_worker(self, targets, msg, user, pwd, cost_per_person):
        """
        ارسال پیامک با پروتکل SOAP (نسخه پایدار و اصلاح شده)
        """
        domain = SMS_CONFIG["DOMAIN"]
        raw_sender = SMS_CONFIG["line_options"][0] if SMS_CONFIG["line_options"] else "+989989000"
        
        # اصلاح فرمت شماره فرستنده
        sender = raw_sender.strip()
        if sender.isdigit():
            if sender.startswith("0"): sender = "+98" + sender[1:]
            elif sender.startswith("98"): sender = "+" + sender
            else: sender = "+98" + sender
            
        success = 0
        failed = 0
        last_error_details = ""
        
        # تنظیمات نشست برای پایداری
        with requests.Session() as s:
            s.trust_env = False
            s.proxies = {"http": None, "https": None}
            
            # استفاده از آداپتور برای تلاش مجدد
            from requests.adapters import HTTPAdapter
            from urllib3.util.retry import Retry
            retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
            s.mount('http://', HTTPAdapter(max_retries=retries))

            url = f"http://{domain}/webservice/send.php"
            
            headers = {
                'Content-Type': 'text/xml; charset=utf-8',
                'SOAPAction': f"http://{domain}/webservice/send.php/SendSMS",
                'User-Agent': 'PHP-SOAP/7.4.33',
                'Connection': 'close' 
            }

            # 1. استعلام اعتبار (برای گرم کردن کانکشن)
            try:
                cred_body = f"""<?xml version="1.0" encoding="UTF-8"?><SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://{domain}/webservice/send.php" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><SOAP-ENV:Body><ns1:GetCredit><Username xsi:type="xsd:string">{user}</Username><Password xsi:type="xsd:string">{pwd}</Password></ns1:GetCredit></SOAP-ENV:Body></SOAP-ENV:Envelope>"""
                s.post(url, data=cred_body.encode('utf-8'), headers={'Content-Type': 'text/xml; charset=utf-8', 'SOAPAction': f"http://{domain}/webservice/send.php/GetCredit", 'Connection': 'close'}, timeout=10)
            except: pass

            # 2. حلقه ارسال
            for p in targets:
                try:
                    # استانداردسازی شماره گیرنده
                    clean_p = ScraperUtils.to_english_digits(str(p))
                    clean_p = re.sub(r'[^0-9]', '', clean_p)
                    if clean_p.startswith("0"): clean_p = clean_p[1:]
                    if not clean_p.startswith("98"): clean_p = "98" + clean_p
                    final_phone = "+" + clean_p
                    
                    soap_body = f"""<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <SOAP-ENV:Body>
        <ns1:SendSMS xmlns:ns1="http://{domain}/webservice/send.php">
            <fromNum xsi:type="xsd:string">{sender}</fromNum>
            <toNum SOAP-ENC:arrayType="xsd:string[1]" xsi:type="SOAP-ENC:Array">
                <item xsi:type="xsd:string">{final_phone}</item>
            </toNum>
            <Content xsi:type="xsd:string">{msg}</Content>
            <Type xsi:type="xsd:string">0</Type>
            <Username xsi:type="xsd:string">{user}</Username>
            <Password xsi:type="xsd:string">{pwd}</Password>
        </ns1:SendSMS>
    </SOAP-ENV:Body>
</SOAP-ENV:Envelope>"""
                    
                    # ارسال درخواست (بدون استفاده از session برای جلوگیری از خطای Prematurely در برخی سرورها)
                    # اگر سرور از Keep-Alive پشتیبانی نکند، requests.post امن‌تر است
                    resp = requests.post(url, data=soap_body.encode('utf-8'), headers=headers, timeout=25, proxies={"http": None, "https": None})
                    
                    resp_content = resp.text
                    
                    # بررسی موفقیت
                    is_fault = "Fault" in resp_content or "Exception" in resp_content
                    match_ret = re.search(r'<return[^>]*>([^<]+)</return>', resp_content)
                    return_val = match_ret.group(1) if match_ret else ""
                    
                    is_success = False
                    if resp.status_code == 200 and not is_fault:
                        if return_val.isdigit() and len(return_val) > 3: is_success = True 
                        elif len(resp_content) > 300: is_success = True 
                    
                    if is_success:
                        success += 1
                        print(f"SMS OK: {final_phone}")
                        # [اصلاح شماره ۵]: لاگ پیامک موفق در دیتابیس برای تقویم
                        DatabaseHandler.log_message(final_phone, msg[:50], "SMS", "موفق", "ارسال پیامک")
                    else:
                        failed += 1
                        err = self._extract_soap_error(resp_content)
                        if not err: err = return_val if return_val else f"Status: {resp.status_code}"
                        last_error_details = err
                        print(f"SMS Failed: {final_phone} -> {err}")
                        # [اصلاح شماره ۶]: لاگ پیامک ناموفق در دیتابیس
                        DatabaseHandler.log_message(final_phone, msg[:50], "SMS", "ناموفق", err[:50])
                        
                except Exception as e:
                    failed += 1
                    last_error_details = str(e)
                    print(f"SMS Exception: {e}")

        # گزارش نهایی
        self.after(0, lambda: self._show_final_report(success, failed, cost_per_person, last_error_details))

    # --- Other Tabs (Standard UI + Range Update) ---
    def setup_social_bulk_tab(self):
        t = self.tabs_tools.add("📢 ارسال انبوه")
        ctk.CTkLabel(t, text="ارسال پیام انبوه در شبکه‌های اجتماعی", font=FONT_TITLE, text_color=THEME["telegram"]).pack(pady=10)
        
        # Platform Select
        ctk.CTkLabel(t, text="پلتفرم مقصد:", anchor="e", font=FONT_NORMAL).pack(fill="x", padx=15)
        self.cmb_social_bulk = ctk.CTkOptionMenu(t, values=["WhatsApp", "Telegram", "Eitaa", "Bale", "Rubika"], 
                                                 fg_color=THEME["bg_input"], button_color=THEME["primary"], font=(APP_FONT, 14))
        self.cmb_social_bulk.pack(fill="x", padx=15, pady=5)
        
        # Product Select
        ctk.CTkLabel(t, text="انتخاب محصول (اختیاری):", anchor="e", font=FONT_NORMAL).pack(fill="x", padx=15)
        prod_names = [p.get('name') for p in AIBrain.PRODUCTS]
        self.cmb_bulk_prod = ctk.CTkComboBox(t, values=["-- انتخاب محصول --"] + prod_names, justify="right", 
                                             command=self.on_bulk_prod_select, font=(APP_FONT, 14))
        self.cmb_bulk_prod.pack(fill="x", padx=15, pady=5)
        
        # Targets
        target_frame = ctk.CTkFrame(t, fg_color=THEME["bg_input"])
        target_frame.pack(fill="x", padx=15, pady=10)
        
        self.chk_social_all = ctk.CTkSwitch(target_frame, text="کل دیتابیس", progress_color=THEME["success"], font=(APP_FONT, 12))
        self.chk_social_all.pack(side="right", padx=10, pady=10)
        
        ctk.CTkButton(target_frame, text="📂 اکسل", width=80, fg_color="#333", font=(APP_FONT, 11), command=self.load_excel_numbers).pack(side="left", padx=10)
        self.lbl_excel_status = ctk.CTkLabel(target_frame, text="", font=(APP_FONT, 10))
        self.lbl_excel_status.pack(side="left")

        # Range Selector Social (NEW)
        range_frame = ctk.CTkFrame(t, fg_color="transparent")
        range_frame.pack(fill="x", padx=15)
        self.chk_range_social = ctk.CTkSwitch(range_frame, text="ارسال بازه‌ای", font=(APP_FONT, 11))
        self.chk_range_social.pack(side="right", padx=5)
        self.ent_range_to_soc = ctk.CTkEntry(range_frame, width=50, placeholder_text="تا"); self.ent_range_to_soc.pack(side="left", padx=5)
        self.ent_range_from_soc = ctk.CTkEntry(range_frame, width=50, placeholder_text="از"); self.ent_range_from_soc.pack(side="left", padx=5)
        add_context_menu(self.ent_range_to_soc)
        add_context_menu(self.ent_range_from_soc)

        # Manual
        ctk.CTkLabel(t, text="افزودن شماره دستی:", anchor="e", font=FONT_SMALL).pack(fill="x", padx=15)
        self.txt_social_manual = ctk.CTkTextbox(t, height=50, fg_color=THEME["bg_input"], text_color="white", font=FONT_MONO)
        self.txt_social_manual.pack(fill="x", padx=15, pady=5)
        add_context_menu(self.txt_social_manual) # افزودن منو راست کلیک
        
        # Message
        ctk.CTkLabel(t, text="متن پیام:", anchor="e", font=FONT_NORMAL).pack(fill="x", padx=15)
        self.txt_social_msg = ctk.CTkTextbox(t, height=80, fg_color=THEME["bg_input"], text_color="white", font=(APP_FONT, 14))
        self.txt_social_msg.pack(fill="x", padx=15, pady=5)
        self.txt_social_msg.tag_config("rtl", justify='right')
        add_context_menu(self.txt_social_msg) # افزودن منو راست کلیک
        
        ctk.CTkButton(t, text="✨ هوش مصنوعی (پیشنهاد متن)", fg_color="transparent", border_width=1, border_color=THEME["primary"], font=(APP_FONT, 12), command=lambda: self.ai_social_msg()).pack(fill="x", padx=15, pady=5)
        
        # Media Picker (New Feature)
        media_frame = ctk.CTkFrame(t, fg_color="transparent")
        media_frame.pack(fill="x", padx=15, pady=5)
        
        self.btn_bulk_media = ctk.CTkButton(media_frame, text="📎 افزودن فایل (عکس/ویدئو)", width=160, 
                                            fg_color=THEME["bg_input"], border_width=1, border_color=THEME["border"],
                                            text_color="gray", hover_color=THEME["bg_hover"],
                                            command=self.pick_bulk_media)
        self.btn_bulk_media.pack(side="right")
        
        self.lbl_bulk_media_status = ctk.CTkLabel(media_frame, text="فایلی انتخاب نشده", font=(APP_FONT, 11), text_color="gray")
        self.lbl_bulk_media_status.pack(side="right", padx=10)

        self.progress_social = ctk.CTkProgressBar(t); self.progress_social.set(0); self.progress_social.pack(fill="x", padx=15, pady=10)
        
        self.btn_start_social = ctk.CTkButton(t, text="🚀 شروع ارسال انبوه", fg_color=THEME["secondary"], height=45, font=(APP_FONT, 15, "bold"), command=self.start_social_bulk)
        self.btn_start_social.pack(fill="x", padx=15, pady=10)
        
        self.lbl_social_status = ctk.CTkLabel(t, text="آماده ارسال", text_color="gray", font=(APP_FONT, 12)); self.lbl_social_status.pack()
        self.bulk_media_path = None

    def pick_bulk_media(self):
        path = filedialog.askopenfilename(filetypes=[("Media Files", "*.jpg;*.jpeg;*.png;*.mp4;*.avi;*.mov")])
        if path:
            self.bulk_media_path = path
            filename = os.path.basename(path)
            if len(filename) > 20: filename = filename[:20] + "..."
            self.lbl_bulk_media_status.configure(text=f"✅ {filename}", text_color=THEME["success"])
            self.btn_bulk_media.configure(border_color=THEME["success"], text_color="white")
        else:
            self.bulk_media_path = None
            self.lbl_bulk_media_status.configure(text="فایلی انتخاب نشده", text_color="gray")
            self.btn_bulk_media.configure(border_color=THEME["border"], text_color="gray")

    def ai_social_msg(self):
        self.txt_social_msg.delete("1.0","end")
        self.txt_social_msg.insert("end", "⏳ هوش مصنوعی در حال نوشتن...", "rtl")
        threading.Thread(target=self._ai_social_thread, daemon=True).start()

    def _ai_social_thread(self):
        # استفاده از متد اصلاح شده با Fallback
        text = AIBrain.generate_marketing_text("Social")
        self.after(0, lambda: self._update_social_text(text))

    def _update_social_text(self, text):
        self.txt_social_msg.delete("1.0","end")
        self.txt_social_msg.insert("end", text, "rtl")

    def setup_products_tab(self):
        t = self.tabs_tools.add("📦 محصولات")
        f = ctk.CTkFrame(t, fg_color=THEME["bg_card"], border_color=THEME["border"], border_width=1)
        f.pack(fill="x", padx=10, pady=10)
        
        self.e_pname = ctk.CTkEntry(f, placeholder_text="نام محصول", justify="right", height=35, font=(APP_FONT, 14))
        self.e_pname.pack(fill="x", pady=5, padx=10)
        
        self.e_pfeat = ctk.CTkEntry(f, placeholder_text="ویژگی‌های کلیدی", justify="right", height=35, font=(APP_FONT, 14))
        self.e_pfeat.pack(fill="x", pady=5, padx=10)
        
        f2 = ctk.CTkFrame(f, fg_color="transparent"); f2.pack(fill="x", pady=5)
        self.e_pprice = ctk.CTkEntry(f2, placeholder_text="قیمت اصلی", justify="right", width=120, font=(APP_FONT, 14))
        self.e_pprice.pack(side="right", padx=10)
        self.e_poff = ctk.CTkEntry(f2, placeholder_text="قیمت تخفیفی", justify="right", width=120, font=(APP_FONT, 14))
        self.e_poff.pack(side="right", padx=10)
        
        add_context_menu(self.e_pname)
        add_context_menu(self.e_pfeat)
        add_context_menu(self.e_pprice)
        add_context_menu(self.e_poff)
        
        f3 = ctk.CTkFrame(f, fg_color="transparent"); f3.pack(fill="x", pady=5)
        self.btn_img = ctk.CTkButton(f3, text="➕ تصویر", width=90, fg_color=THEME["bg_input"], command=self.pick_image, font=(APP_FONT, 12))
        self.btn_img.pack(side="right", padx=10)
        self.btn_vid = ctk.CTkButton(f3, text="➕ ویدئو", width=90, fg_color=THEME["bg_input"], command=self.pick_video, font=(APP_FONT, 12))
        self.btn_vid.pack(side="right", padx=10)
        
        self.lbl_media_status = ctk.CTkLabel(f3, text="مدیا: ندارد", text_color="gray", font=(APP_FONT, 10))
        self.lbl_media_status.pack(side="left", padx=10)
        
        ctk.CTkButton(t, text="افزودن به کاتالوگ", fg_color=THEME["success"], height=40, font=(APP_FONT, 13, "bold"), command=self.add_prod).pack(fill="x", padx=10, pady=10)
        
        list_frame = ctk.CTkFrame(t, fg_color="transparent")
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        cols = ("name", "price")
        self.prod_tree = ttk.Treeview(list_frame, columns=cols, show="headings", height=8)
        self.prod_tree.heading("name", text="نام محصول"); self.prod_tree.column("name", width=120, anchor="e")
        self.prod_tree.heading("price", text="قیمت"); self.prod_tree.column("price", width=80, anchor="center")
        self.prod_tree.pack(fill="both", expand=True)
        self.refresh_prod_list()

    def setup_bot_tab(self):
        t = self.tabs_tools.add("🤖 ربات")
        ctk.CTkLabel(t, text="کنترل پنل ربات پاسخگو", font=FONT_TITLE, text_color=THEME["info"]).pack(pady=15)
        
        ctk.CTkLabel(t, text="انتخاب پلتفرم:", anchor="e", font=FONT_NORMAL).pack(fill="x", padx=20)
        self.cmb_bot = ctk.CTkComboBox(t, values=["WhatsApp", "Telegram", "Eitaa", "Bale", "Rubika"], justify="right", height=35, font=(APP_FONT, 14))
        self.cmb_bot.pack(fill="x", padx=20, pady=5)
        
        status_frame = ctk.CTkFrame(t, fg_color=THEME["bg_card"], height=80)
        status_frame.pack(fill="x", padx=20, pady=20)
        self.lbl_bot_status = ctk.CTkLabel(status_frame, text="وضعیت: غیرفعال", text_color="gray", font=(APP_FONT, 13, "bold"))
        self.lbl_bot_status.pack(pady=25)
        
        ctk.CTkButton(t, text="▶️ شروع ربات", fg_color=THEME["success"], height=45, font=(APP_FONT, 15, "bold"), command=self.start_bot).pack(fill="x", padx=20, pady=10)
        ctk.CTkButton(t, text="⏹️ توقف اجباری", fg_color=THEME["danger"], height=45, font=(APP_FONT, 15, "bold"), command=self.stop_bot).pack(fill="x", padx=20, pady=10)

    # =================================================================
    #  LOGIC FUNCTIONS (UNCHANGED BUT INCLUDED FOR COMPLETENESS)
    # =================================================================
    def load_excel_numbers(self):
        path = filedialog.askopenfilename(filetypes=[("Excel/CSV", "*.xlsx;*.xls;*.csv")])
        if not path: return
        try:
            if path.endswith('.csv'): df = pd.read_csv(path)
            else: df = pd.read_excel(path)
            target_col = next((c for c in df.columns if any(x in str(c).lower() for x in ['phone', 'mobile', 'tel', 'تلفن', 'موبایل', 'شماره'])), df.columns[0])
            nums = df[target_col].dropna().astype(str).tolist()
            self.excel_numbers = [ScraperUtils.to_english_digits(n) for n in nums]
            messagebox.showinfo("موفق", f"{len(self.excel_numbers)} شماره بارگذاری شد.")
            self.lbl_excel_status.configure(text=f"فایل: {len(self.excel_numbers)}")
        except Exception as e: messagebox.showerror("خطا", f"خطا در خواندن فایل:\n{e}")

    def load_excel_numbers_sms(self):
        path = filedialog.askopenfilename(filetypes=[("Excel/CSV", "*.xlsx;*.xls;*.csv")])
        if not path: return
        try:
            if path.endswith('.csv'): df = pd.read_csv(path)
            else: df = pd.read_excel(path)
            target_col = next((c for c in df.columns if any(x in str(c).lower() for x in ['phone', 'mobile', 'tel', 'تلفن', 'موبایل', 'شماره'])), df.columns[0])
            nums = df[target_col].dropna().astype(str).tolist()
            self.excel_numbers_sms = [ScraperUtils.to_english_digits(n) for n in nums]
            self.lbl_sms_excel_stat.configure(text=f"✅ {len(self.excel_numbers_sms)} شماره", text_color=THEME["success"])
            messagebox.showinfo("موفق", f"{len(self.excel_numbers_sms)} شماره برای پیامک بارگذاری شد.")
        except Exception as e: messagebox.showerror("خطا", f"خطا در خواندن فایل:\n{e}")

    def on_bulk_prod_select(self, val):
        if val == "-- انتخاب محصول --": 
            # اگر محصولی انتخاب نشود، فایل انتخابی کاربر باقی می‌ماند
            return
        prod = next((p for p in AIBrain.PRODUCTS if p.get('name') == val), None)
        if prod:
            text = f"🔥 پیشنهاد ویژه: {prod.get('name')}\n\n✅ {prod.get('features')}\n\n💰 قیمت: {prod.get('price_off')} تومان (تخفیف ویژه)\n\n📍 همین الان سفارش دهید!"
            self.txt_social_msg.delete("1.0", "end"); self.txt_social_msg.insert("end", text, "rtl")
            if prod.get('video') and os.path.exists(prod.get('video')): 
                self.bulk_media_path = prod.get('video')
                self.lbl_bulk_media_status.configure(text=f"📎 ویدئو محصول پیوست شد", text_color=THEME["info"])
            elif prod.get('image') and os.path.exists(prod.get('image')): 
                self.bulk_media_path = prod.get('image')
                self.lbl_bulk_media_status.configure(text=f"📎 تصویر محصول پیوست شد", text_color=THEME["info"])
            else: 
                # اگر محصول مدیا نداشت، مدیای قبلی پاک نمی‌شود تا شاید کاربر دستی انتخاب کرده باشد
                pass

    def pick_image(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg;*.jpeg;*.png")])
        if path: self.current_prod_img = path; self.lbl_media_status.configure(text="✅ تصویر انتخاب شد")
    def pick_video(self):
        path = filedialog.askopenfilename(filetypes=[("Videos", "*.mp4;*.avi;*.mov")])
        if path: self.current_prod_vid = path; self.lbl_media_status.configure(text="✅ ویدئو انتخاب شد")
    def add_prod(self):
        p = {"name": self.e_pname.get(), "features": self.e_pfeat.get(), "price_main": self.e_pprice.get(), "price_off": self.e_poff.get(), "image": self.current_prod_img, "video": self.current_prod_vid}
        if p["name"]:
            AIBrain.PRODUCTS.append(p); AIBrain.save(new_products=AIBrain.PRODUCTS)
            self.e_pname.delete(0,'end'); self.e_pfeat.delete(0,'end'); self.e_pprice.delete(0,'end'); self.e_poff.delete(0,'end')
            self.current_prod_img = None; self.current_prod_vid = None; self.lbl_media_status.configure(text="مدیا: ندارد"); self.refresh_prod_list(); messagebox.showinfo("موفق", "محصول ذخیره شد.")
    def refresh_prod_list(self):
        for i in self.prod_tree.get_children(): self.prod_tree.delete(i)
        for p in AIBrain.PRODUCTS: self.prod_tree.insert("", "end", values=(p.get('name'), p.get('price_main')))

    # ai_sms removed here as it is in SMS tab part now

    def start_bot(self):
        plat = self.cmb_bot.get()
        self.bot = SmartChatBot(plat, lambda m, l: self.lbl_bot_status.configure(text=m[:40], text_color="white" if l=="info" else THEME["success"]))
        if self.bot.start(): threading.Thread(target=self.bot.loop, daemon=True).start(); self.lbl_bot_status.configure(text="🟢 ربات فعال است", text_color=THEME["success"])
    def stop_bot(self):
        if self.bot: self.bot.stop_signal = True; self.lbl_bot_status.configure(text="🔴 متوقف شد", text_color="red")

    def start_social_bulk(self):
        msg = self.txt_social_msg.get("1.0","end").strip(); 
        if not msg: messagebox.showerror("خطا", "لطفاً متن پیام را وارد کنید."); return
        platform = self.cmb_social_bulk.get()
        targets = []
        
        # 1. Database (Full or Range)
        if self.chk_social_all.get() or self.chk_range_social.get():
            active_tab = self.tabs_db.get()
            if active_tab not in self.TABLE_MAP: messagebox.showerror("خطا", "لطفاً یک جدول معتبر انتخاب کنید."); return
            table = self.TABLE_MAP.get(active_tab)
            all_phones = DatabaseHandler.fetch_phones(table)
            
            if self.chk_range_social.get():
                try:
                    s = int(self.ent_range_from_soc.get())
                    e = int(self.ent_range_to_soc.get())
                    if s<1: s=1
                    targets.extend(all_phones[s-1:e])
                except: messagebox.showerror("خطا", "بازه نامعتبر"); return
            else:
                targets.extend(all_phones)

        # 2. Excel & Manual
        targets += self.excel_numbers
        manual_text = self.txt_social_manual.get("1.0", "end").strip()
        if manual_text: manual_list = re.split(r'[,\n\r]+', manual_text); targets += [ScraperUtils.to_english_digits(m.strip()) for m in manual_list if m.strip()]
        
        targets = ScraperUtils.uniq(targets)
        if not targets: messagebox.showerror("خطا", "شماره‌ای یافت نشد."); return
        
        if messagebox.askyesno("تایید ارسال", f"مقصد: {platform}\nتعداد: {len(targets)}"):
            self.btn_start_social.configure(state="disabled")
            threading.Thread(target=self._social_bulk_worker, args=(platform, targets, msg, self.bulk_media_path)).start()

    def _social_bulk_worker(self, platform, targets, msg, media_file):
        # دریافت تنظیمات پیشرفته ربات
        bot_config = AIBrain.DATA.get("bot_config", {})
        delay_min = int(bot_config.get("delay_min", 10))
        delay_max = int(bot_config.get("delay_max", 25))
        
        # بارگذاری پیام‌های متغیر
        variable_messages = []
        raw_vars = bot_config.get("message_variations", "")
        if raw_vars:
            variable_messages = [m.strip() for m in raw_vars.split("|||") if m.strip()]
        
        # UI Setup
        self.after(0, lambda: self.lbl_social_status.configure(text="⏳ راه‌اندازی مرورگر...", text_color=THEME["warning"]))
        
        bot = SmartChatBot(platform, lambda m, l: print(f"Bot: {m}"))
        
        if not bot.start(): 
            self.after(0, lambda: [
                self.lbl_social_status.configure(text="❌ خطا در باز کردن مرورگر", text_color=THEME["danger"]),
                self.btn_start_social.configure(state="normal")
            ])
            return
            
        # --- LOGIN CHECK ---
        wait_time = 60 if platform == "Bale" else 120
        wait_msg = "۱ دقیقه" if platform == "Bale" else "۲ دقیقه"
        
        self.after(0, lambda: self.lbl_social_status.configure(text=f"🔑 لطفاً وارد حساب خود شوید (حداکثر {wait_msg})...", text_color=THEME["info"]))
        
        if bot.wait_for_login(timeout=wait_time):
            self.after(0, lambda: self.lbl_social_status.configure(text="✅ ورود تایید شد. شروع ارسال...", text_color=THEME["success"]))
            time.sleep(3) # مکث کوتاه قبل از شروع
        else:
            if platform == "Bale":
                # در بله بدون توجه به تایم‌اوت ادامه می‌دهیم (شروع اجباری ارسال)
                self.after(0, lambda: self.lbl_social_status.configure(text="⚠️ زمان بررسی گذشت. تلاش برای ارسال اجباری...", text_color=THEME["warning"]))
            else:
                bot.stop()
                self.after(0, lambda: [
                    self.lbl_social_status.configure(text="❌ عدم تشخیص ورود (تایم‌اوت)", text_color=THEME["danger"]),
                    self.btn_start_social.configure(state="normal"),
                    messagebox.showerror("خطا", "زمان انتظار برای ورود به پایان رسید.\nلطفاً سریعتر اسکن کنید یا وارد شوید.")
                ])
                return

        # شروع حلقه ارسال
        total = len(targets); success_count = 0
        
        for i, phone in enumerate(targets):
            if bot.stop_signal: break
            
            final_msg = msg
            if variable_messages:
                final_msg = random.choice(variable_messages)
            
            progress_val = (i + 1) / total
            status_text = f"ارسال {i+1} از {total}..."
            self.after(0, lambda p=progress_val, t=status_text: [
                self.progress_social.set(p),
                self.lbl_social_status.configure(text=t, text_color="white")
            ])
            
            try:
                status, log_msg = bot.send_to_number(phone, final_msg, media_file)
                if status: 
                    success_count += 1
                    # [اصلاح شماره ۷]: همگام سازی ارسال انبوه شبکه‌های اجتماعی با تقویم
                    DatabaseHandler.log_message(phone, final_msg[:50], platform, "موفق", "ارسال انبوه")
                else:
                    DatabaseHandler.log_message(phone, final_msg[:50], platform, "ناموفق", log_msg[:50])
                
                print(f"Send Report [{phone}]: {status} - {log_msg}")

                wait_time = random.uniform(delay_min, delay_max)
                time.sleep(wait_time)
                
            except Exception as e: 
                print(f"Loop Error: {e}")
            
        bot.stop()
        self.after(0, lambda: [
            self.progress_social.set(1.0),
            self.lbl_social_status.configure(text=f"پایان. موفق: {success_count}", text_color=THEME["success"]),
            messagebox.showinfo("پایان عملیات", f"ارسال انبوه به پایان رسید.\n✅ موفق: {success_count}\n❌ ناموفق: {total - success_count}"),
            self.btn_start_social.configure(state="normal")
        ])

class AIConfigFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=THEME["bg_root"])
        self.entries = {}
        AIBrain.load() 
        self.build_ui()
        
    def build_ui(self):
        # Header
        ctk.CTkLabel(
            self, 
            text="🧠 هوش تجاری و تنظیمات پرمیوم", 
            font=FONT_HEADER, 
            text_color=THEME["primary"]
        ).pack(pady=20)
        
        ctk.CTkLabel(
            self, 
            text="تنظیمات زیر رفتار ربات پاسخگو را کنترل می‌کنند:", 
            font=FONT_SMALL, 
            text_color="gray"
        ).pack(pady=(0, 10))
        
        # Scrollable Form Area
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=50, pady=10)
        
        fields = [
            ("نام کسب‌وکار", "business_name"), 
            ("زمینه فعالیت", "category"), 
            ("نوع کسب‌وکار (خدماتی/فروشگاهی)", "business_type"), 
            ("منطق اقتصادی (قیمت/کیفیت)", "economic_logic"), 
            ("مخاطب هدف", "target_audience"), 
            ("هدف فروش", "sales_goal"), 
            ("مزیت رقابتی (USP)", "usp"), 
            ("استراتژی پاسخ به اعتراضات", "objection_handling"), 
            ("آفرهای ویژه", "offers"), 
            ("اطلاعات تماس", "contact_info"), 
            ("لحن ربات", "tone"), 
            ("پرسونا (شخصیت)", "persona"), 
            ("کلمات ممنوعه", "forbidden_words")
        ]
        
        for lbl, key in fields:
            row_frame = ctk.CTkFrame(scroll, fg_color="transparent")
            row_frame.pack(fill="x", pady=5)
            
            # RTL Label (Right side)
            ctk.CTkLabel(
                row_frame, 
                text=lbl, 
                width=200, 
                anchor="e", 
                font=FONT_NORMAL
            ).pack(side="right", padx=10)
            
            # Entry (Left side)
            entry = ctk.CTkEntry(
                row_frame, 
                justify="right", 
                fg_color=THEME["bg_input"], 
                height=35, 
                font=FONT_NORMAL
            )
            entry.pack(side="left", fill="x", expand=True)
            entry.insert(0, str(AIBrain.DATA.get(key, "")))
            self.entries[key] = entry
            add_context_menu(entry) # افزودن کلیک راست
            
        # Save Button
        ctk.CTkButton(
            self, 
            text="💾 ذخیره تنظیمات هوشمند", 
            height=50, 
            fg_color=THEME["success"], 
            font=FONT_TITLE, 
            command=self.save
        ).pack(pady=20, fill="x", padx=100)

    def save(self):
        data = {k: v.get() for k, v in self.entries.items()}
        AIBrain.save(new_data=data)
        messagebox.showinfo("موفق", "مغز هوشمند با اطلاعات تجاری جدید بروزرسانی شد.")


# =================================================================
#                  MODULE 11: SUPPORT UI (ADDED)
# =================================================================
class SupportFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=THEME["bg_root"])
        # ایجاد جدول در ترد جداگانه تا UI را بلاک نکند
        threading.Thread(target=SupportManager.create_table_if_not_exists, daemon=True).start()
        self.build_ui()

    def build_ui(self):
        # تنظیمات شبکه (Grid) برای تقسیم صفحه به دو بخش چپ و راست
        self.grid_columnconfigure(0, weight=1) # پنل اطلاعات (چپ - در حالت RTL می‌شود راست بصورت بصری)
        self.grid_columnconfigure(1, weight=3) # پنل تیکت‌ها (راست - فضای بیشتر)
        self.grid_rowconfigure(0, weight=1)

        # --- Left Column: Company Info ---
        # استفاده از Frame ثابت برای منوی کناری اطلاعات
        left_panel = ctk.CTkFrame(self, fg_color=THEME["bg_sidebar"], corner_radius=0, width=280)
        left_panel.grid(row=0, column=0, sticky="nsew")
        left_panel.pack_propagate(False) # جلوگیری از تغییر سایز خودکار

        ctk.CTkLabel(left_panel, text="🏢 رایان تکرو", font=(APP_FONT, 22, "bold"), text_color=THEME["primary"]).pack(pady=(40, 20))
        
        info_text = (
            "شرکت توسعه نرم‌افزار رایان تکرو\n"
            "پیشرو در ارائه راهکارهای هوشمند\n\n"
            "📍 آدرس:\n"
            "تبریز، خیابان آزادی\n"
            "جنب شهرداری منطقه 3، طبقه 3\n\n"
            "📞 تلفن تماس:\n"
            "041-34401179\n\n"
            "✉️ ایمیل پشتیبانی:\n"
            "support@winbots.ir"
        )
        ctk.CTkLabel(left_panel, text=info_text, font=(APP_FONT, 14), text_color="white", justify="center").pack(pady=20)
        ctk.CTkLabel(left_panel, text="ساعات پاسخگویی:\nشنبه تا چهارشنبه ۹ الی ۱۷", font=(APP_FONT, 12), text_color="gray").pack(side="bottom", pady=40)

        # --- Right Column: Ticket System ---
        right_panel = ctk.CTkFrame(self, fg_color="transparent")
        right_panel.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Header
        head_frame = ctk.CTkFrame(right_panel, fg_color="transparent")
        head_frame.pack(fill="x", pady=(0, 20))
        ctk.CTkLabel(head_frame, text="مرکز پشتیبانی و تیکتینگ (آنلاین)", font=FONT_HEADER, text_color="white").pack(side="right")
        ctk.CTkButton(head_frame, text="🔄 بروزرسانی", width=100, command=self.refresh_tickets, fg_color=THEME["info"]).pack(side="left")

        # Messages Area (Chat Style)
        self.msg_scroll = ctk.CTkScrollableFrame(right_panel, fg_color=THEME["bg_card"], label_text="لیست تیکت‌های شما", label_font=(APP_FONT, 12, "bold"))
        self.msg_scroll.pack(fill="both", expand=True, pady=(0, 20))

        # Input Area (Form)
        input_frame = ctk.CTkFrame(right_panel, fg_color=THEME["bg_input"])
        input_frame.pack(fill="x", ipady=10)

        ctk.CTkLabel(input_frame, text="موضوع:", font=FONT_NORMAL).pack(anchor="e", padx=15, pady=(10, 0))
        self.ent_subject = ctk.CTkEntry(input_frame, justify="right", font=FONT_NORMAL)
        self.ent_subject.pack(fill="x", padx=15, pady=(5, 10))
        add_context_menu(self.ent_subject)

        ctk.CTkLabel(input_frame, text="متن پیام:", font=FONT_NORMAL).pack(anchor="e", padx=15)
        self.txt_msg = ctk.CTkTextbox(input_frame, height=80, font=FONT_NORMAL)
        self.txt_msg.pack(fill="x", padx=15, pady=(5, 15))
        add_context_menu(self.txt_msg)
        # RTL Config for Textbox
        try: self.txt_msg.tag_config("rtl", justify='right')
        except: pass

        self.btn_send = ctk.CTkButton(input_frame, text="ارسال تیکت", fg_color=THEME["success"], height=40, font=(APP_FONT, 14, "bold"), command=self.send_ticket)
        self.btn_send.pack(fill="x", padx=15, pady=(0, 15))

    def refresh_tickets(self):
        # پاک کردن ویجت‌های قبلی
        for w in self.msg_scroll.winfo_children(): w.destroy()
        
        # نمایش لودینگ
        loading_lbl = ctk.CTkLabel(self.msg_scroll, text="⏳ در حال دریافت اطلاعات از سرور...", text_color="gray")
        loading_lbl.pack(pady=20)
        
        # دریافت اطلاعات در ترد پس‌زمینه
        threading.Thread(target=self._load_tickets_thread, args=(loading_lbl,), daemon=True).start()

    def _load_tickets_thread(self, loading_lbl):
        tickets = SupportManager.fetch_tickets()
        # آپدیت UI در ترد اصلی
        self.after(0, lambda: self._render_tickets(tickets, loading_lbl))

    def _render_tickets(self, tickets, loading_lbl):
        loading_lbl.destroy()
        
        if not tickets:
            ctk.CTkLabel(self.msg_scroll, text="هیچ تیکتی یافت نشد.", text_color="gray", font=FONT_NORMAL).pack(pady=20)
            return

        for t in tickets:
            card = ctk.CTkFrame(self.msg_scroll, fg_color=THEME["bg_root"], border_color=THEME["border"], border_width=1)
            card.pack(fill="x", pady=5, padx=5)

            # Header Row
            head = ctk.CTkFrame(card, fg_color="transparent")
            head.pack(fill="x", padx=10, pady=5)
            
            status_map = {'open': 'در انتظار پاسخ', 'closed': 'بسته شده', 'answered': 'پاسخ داده شده'}
            status_text = status_map.get(t['status'], t['status'])
            status_color = THEME["warning"] if t['status'] == 'open' else THEME["success"]
            
            if t.get('admin_reply'): 
                status_text = "✅ پاسخ داده شده"
                status_color = THEME["success"]

            ctk.CTkLabel(head, text=t['subject'], font=(APP_FONT, 13, "bold"), text_color="white").pack(side="right")
            
            # Badge وضعیت
            status_badge = ctk.CTkLabel(head, text=f" {status_text} ", fg_color=status_color, text_color="black", corner_radius=6, font=(APP_FONT, 10, "bold"))
            status_badge.pack(side="left")

            # متن پیام کاربر
            ctk.CTkLabel(card, text=t['message'], font=(APP_FONT, 12), text_color="#DDD", justify="right", wraplength=450).pack(anchor="e", padx=10, pady=5)
            ctk.CTkLabel(card, text=str(t['created_at']), font=("vazir", 9), text_color="gray").pack(anchor="w", padx=10, pady=(0,5))

            # پاسخ ادمین
            if t.get('admin_reply'):
                reply_frame = ctk.CTkFrame(card, fg_color=THEME["bg_input"], corner_radius=5)
                reply_frame.pack(fill="x", padx=10, pady=10)
                ctk.CTkLabel(reply_frame, text="👤 پاسخ پشتیبانی:", font=(APP_FONT, 11, "bold"), text_color=THEME["secondary"]).pack(anchor="e", padx=5, pady=(5,0))
                ctk.CTkLabel(reply_frame, text=t['admin_reply'], font=(APP_FONT, 11), text_color="white", justify="right", wraplength=430).pack(anchor="e", padx=5, pady=5)

    def send_ticket(self):
        subj = self.ent_subject.get().strip()
        msg = self.txt_msg.get("1.0", "end").strip()
        
        if not subj or not msg:
            messagebox.showerror("خطا", "لطفاً موضوع و متن پیام را وارد کنید.")
            return

        self.btn_send.configure(state="disabled", text="در حال ارسال...")
        threading.Thread(target=self._send_thread, args=(subj, msg), daemon=True).start()

    def _send_thread(self, subj, msg):
        success, resp = SupportManager.send_ticket(subj, msg)
        self.after(0, lambda: self._post_send(success, resp))

    def _post_send(self, success, resp):
        self.btn_send.configure(state="normal", text="ارسال تیکت")
        if success:
            messagebox.showinfo("موفق", resp)
            self.ent_subject.delete(0, "end")
            self.txt_msg.delete("1.0", "end")
            self.refresh_tickets()
        else:
            messagebox.showerror("خطا", resp)

# =================================================================
#                  MAIN APPLICATION CLASS (UPDATED SIDEBAR)
# =================================================================
class WinboApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("WINBO ENTERPRISE ULTIMATE V24.5 - DIAMOND PRO EDITION")
        self.geometry("1400x900")
        
        # تنظیم آیکون در صورت وجود
        try:
            icon_path = resource_path(os.path.join("assest", "logo.ico"))
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)
        except: pass
        
        # جلوگیری از خطای invalid command در زمان بستن اپلیکیشن
        self.protocol("WM_DELETE_WINDOW", self.safe_exit)
        
        # تعریف متغیرهای پایه جهت جلوگیری از کرش شدن رابط کاربری
        self.ui_initialized = False
        self.frames = {}

    def safe_exit(self):
        """خروج ایمن و پاکسازی کامل تردها برای جلوگیری از خطای Tkinter"""
        try:
            self.quit()
            self.destroy()
            os._exit(0)
        except: pass

    def init_ui(self):
        """رندر کردن رابط کاربری اصلی فقط بعد از لاگین موفق برای خواندن دیتای دقیق"""
        # بررسی ایمن برای جلوگیری از رندر مجدد (جلوگیری از خطای AttributeError)
        if getattr(self, 'ui_initialized', False): return
        
        # ساختار کلی (هدر با اطلاعات واقعی ساخته می‌شود)
        self.build_header()
        
        # سایدبار سمت راست (RTL)
        self.sidebar = ctk.CTkFrame(self, width=260, fg_color=THEME["bg_sidebar"], corner_radius=0)
        self.sidebar.pack(side="right", fill="y")
        self.build_sidebar()

        # فضای اصلی سمت چپ
        self.main_area = ctk.CTkFrame(self, fg_color=THEME["bg_root"])
        self.main_area.pack(side="left", fill="both", expand=True)
        
        # ثبت وضعیت رندر شدن رابط کاربری
        self.ui_initialized = True
        
        # پیش‌فرض داشبورد باز شود
        self.show_frame("dashboard")

    def build_header(self):
        lic = LicenseManager.USER_CONTEXT
        
        # اگر لایسنس منقضی شده باشد یا days_left صفر باشد
        try:
            days = int(lic.get('days_left', 0))
            is_active = lic.get('is_active', False)
        except: days = 0; is_active = False
        
        status_color = THEME["success"] if is_active and days > 0 else THEME["danger"]
        status_text = "فعال" if is_active and days > 0 else "منقضی شده ⛔"

        head = ctk.CTkFrame(self, height=70, fg_color=THEME["bg_card"], corner_radius=0)
        head.pack(side="top", fill="x")
        
        # لوگوی هدر
        logo_path = resource_path(os.path.join("assest", "logo.png"))
        logo_loaded = False
        
        if os.path.exists(logo_path):
            try:
                pil_img = Image.open(logo_path)
                header_img = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(40, 40))
                
                logo_container = ctk.CTkFrame(head, fg_color="transparent")
                logo_container.pack(side="left", padx=20)
                
                ctk.CTkLabel(logo_container, text="", image=header_img).pack(side="left")
                ctk.CTkLabel(logo_container, text="WINBO DIAMOND", font=("vazir", 16, "bold"), text_color="white").pack(side="left", padx=10)
                logo_loaded = True
            except: pass
            
        if not logo_loaded:
            ctk.CTkLabel(head, text="WINBO DIAMOND", font=("vazir", 16, "bold"), text_color="white").pack(side="left", padx=30)
        
        # بج‌های اطلاعات کاربر
        info_frame = ctk.CTkFrame(head, fg_color="transparent")
        info_frame.pack(side="right", padx=30)
        
        def _badge(text, color):
            f = ctk.CTkFrame(info_frame, fg_color=color, corner_radius=15, height=30)
            f.pack(side="right", padx=5)
            ctk.CTkLabel(f, text=text, text_color="#000", font=("Vazir", 12, "bold")).pack(padx=10, pady=2)
            
        _badge(f"وضعیت: {status_text}", status_color) 
        
        # نمایش هوشمند زمان انقضا
        if days > 3000:
            _badge("انقضا: نامحدود ♾️", THEME["warning"])
        else:
            exp_date = lic.get('expiry_date', '')
            _badge(f"انقضا: {days} روز ({exp_date})", THEME["warning"])
            
        _badge(lic.get('plan', 'Diamond'), THEME["primary"])
        _badge(lic.get('customer_name', 'کاربر مهمان'), THEME["secondary"])

    def build_sidebar(self):
        # لوگوی سایدبار
        logo_path = resource_path(os.path.join("assest", "logo.png"))
        logo_loaded = False
        
        if os.path.exists(logo_path):
            try:
                pil_img = Image.open(logo_path)
                my_image = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(100, 100))
                ctk.CTkLabel(self.sidebar, text="", image=my_image).pack(pady=(30, 10))
                logo_loaded = True
            except: pass
            
        if not logo_loaded:
            ctk.CTkLabel(self.sidebar, text="WINBO", font=("vazir", 35, "bold"), text_color=THEME["primary"]).pack(pady=(40, 10))

        ctk.CTkLabel(self.sidebar, text="دستیار هوشمند مارکتینگ", font=("Vazir", 12), text_color=THEME["text_dim"]).pack(pady=(0, 30))

        # بررسی وضعیت لایسنس برای قفل کردن منوها
        lic = LicenseManager.USER_CONTEXT
        try:
            is_expired = int(lic.get('days_left', 0)) <= 0 or not lic.get('is_active', False)
        except: is_expired = True
        
        purchased_bots = lic.get('purchased_bots', [])

        menus = [
            ("داشبورد مدیریتی", "dashboard", "📈", None), 
            ("کیف پول دیجیتال", "wallet", "💰", None), 
            ("هاب ربات‌ها", "robots_hub", "🤖", None), 
            ("تنظیمات ربات", "bot_settings", "⚙️", None),
            ("کارخانه محتوایی", "content_factory", "🏭", 11),
            ("مدیریت CRM", "crm", "👥", None), 
            ("هوش تجاری (AI)", "ai", "🧠", 12), 
            ("گزارشات جامع", "reports", "📊", None), 
            ("پشتیبانی و تیکت", "support", "🎧", None), 
        ]
        
        for txt, key, icon, req_bot in menus:
            text_color = "white"
            fg_color = "transparent"
            is_locked = False
            
            # منطق قفل کردن: منقضی شده یا ماژول خریداری نشده
            if is_expired and key not in ["wallet", "support", "dashboard"]:
                is_locked = True
            elif req_bot is not None and req_bot not in purchased_bots:
                is_locked = True
            
            if is_locked:
                text_color = "gray"
                icon = "🔒"
            
            btn = ctk.CTkButton(
                self.sidebar, 
                text=f"  {txt}  {icon}", 
                fg_color=fg_color, 
                hover_color=THEME["bg_hover"] if not is_locked else THEME["bg_sidebar"], 
                anchor="e", 
                height=45, 
                font=FONT_NORMAL,
                text_color=text_color,
                command=lambda k=key, l=is_locked: self.handle_menu_click(k, l)
            )
            btn.pack(fill="x", padx=15, pady=3)
            
        ctk.CTkButton(self.sidebar, text="خروج از حساب", fg_color=THEME["danger"], height=40, font=(APP_FONT, 12, "bold"), command=self.safe_exit).pack(side="bottom", fill="x", padx=20, pady=20)

    def show_frame(self, key):
        # مخفی کردن تمام فریم‌ها
        for w in self.main_area.winfo_children():
            w.pack_forget()
            
        # ساخت فریم اگر وجود نداشت (Lazy Loading)
        if key not in self.frames:
            if key == "dashboard": self.frames[key] = DashboardProFrame(self.main_area)
            elif key == "wallet": self.frames[key] = WalletFrame(self.main_area) 
            elif key == "robots_hub": self.frames[key] = RobotsHubFrame(self.main_area, self) 
            elif key == "bot_settings": self.frames[key] = BotSettingsFrame(self.main_area) 
            elif key == "content_factory": self.frames[key] = ContentFactoryFrame(self.main_area)
            elif key == "crm": self.frames[key] = CRMFrame(self.main_area)
            elif key == "ai": self.frames[key] = AIConfigFrame(self.main_area)
            elif key == "reports": self.frames[key] = ReportsFrame(self.main_area)
            elif key == "support": self.frames[key] = SupportFrame(self.main_area) 
            elif key == "torob": self.frames[key] = TorobUltimateFrame(self.main_area)
            elif key == "instagram": self.frames[key] = InstagramUltimateFrame(self.main_area)
            elif key == "divar": self.frames[key] = DivarUltimateFrame(self.main_area)
            elif key == "sheypoor": self.frames[key] = SheypoorUltimateFrame(self.main_area)
            elif key == "buskool": self.frames[key] = BuskoolUltimateFrame(self.main_area)
            elif key == "neshan": self.frames[key] = NeshanUltimateFrame(self.main_area)
            elif key == "niazrooz": self.frames[key] = NiazroozUltimateFrame(self.main_area)
            elif key == "maps": self.frames[key] = MapsUltimateFrame(self.main_area)
            elif key == "avval": self.frames[key] = AvvalUltimateFrame(self.main_area)
            elif key == "irantejarat": self.frames[key] = IranTejaratUltimateFrame(self.main_area)
            else: self.frames[key] = ctk.CTkLabel(self.main_area, text="به زودی...", font=("Vazir", 30))
            
        # نمایش فریم انتخاب شده
        self.frames[key].pack(fill="both", expand=True)

        # سینک زنده موجودی کیف پول و اطلاعات داشبورد
        if key in ["dashboard", "wallet", "robots_hub"]:
            LicenseManager.refresh_wallet_balance()
        
        # بروزرسانی اطلاعات هر صفحه هنگام باز شدن
        if key == "dashboard" and hasattr(self.frames[key], 'refresh_data'): 
            self.frames[key].refresh_data()
        if key == "wallet" and hasattr(self.frames[key], 'refresh_wallet'): 
            self.frames[key].refresh_wallet() 
        if key == "reports" and hasattr(self.frames[key], 'load_data'): 
            self.frames[key].load_data()
        if key == "support" and hasattr(self.frames[key], 'refresh_tickets'): 
            self.frames[key].refresh_tickets()

    def handle_menu_click(self, key, is_locked):
        if is_locked:
            if key in ["content_factory", "ai"]:
                msg = "این ماژول پیشرفته در لایسنس شما فعال نیست.\nبرای استفاده از این بخش، باید ماژول مربوطه را از مارکت تهیه کنید."
            else:
                msg = "اعتبار لایسنس شما به پایان رسیده است.\nلطفاً برای دسترسی به این بخش، لایسنس خود را تمدید کنید."
            
            if messagebox.askyesno("دسترسی محدود", f"{msg}\n\nآیا می‌خواهید به صفحه فروشگاه هدایت شوید؟"):
                webbrowser.open("https://winboots.ir/user.php?page=market")
            return
        self.show_frame(key)

class BotSettingsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=THEME["bg_root"])
        self.build_ui()

    def build_ui(self):
        config = AIBrain.DATA.get("bot_config", {"delay_min": 10, "delay_max": 25, "ai_variation_enabled": False, "ai_variation_count": 20})
        
        ctk.CTkLabel(self, text="⚙️ تنظیمات پیشرفته ربات", font=FONT_HEADER, text_color=THEME["primary"]).pack(pady=30)
        
        main_card = ctk.CTkFrame(self, fg_color=THEME["bg_card"], corner_radius=15)
        main_card.pack(fill="both", expand=True, padx=50, pady=20)
        
        # Timing
        ctk.CTkLabel(main_card, text="⏱️ زمان‌بندی (ثانیه)", font=FONT_TITLE, text_color=THEME["info"]).pack(anchor="e", padx=30, pady=(30, 10))
        time_frame = ctk.CTkFrame(main_card, fg_color="transparent")
        time_frame.pack(fill="x", padx=30)
        
        self.ent_min = ctk.CTkEntry(time_frame, width=60, justify="center")
        self.ent_min.insert(0, str(config.get("delay_min", 10)))
        self.ent_min.pack(side="left", padx=5)
        add_context_menu(self.ent_min)
        ctk.CTkLabel(time_frame, text="تا", font=FONT_NORMAL).pack(side="left")
        
        self.ent_max = ctk.CTkEntry(time_frame, width=60, justify="center")
        self.ent_max.insert(0, str(config.get("delay_max", 25)))
        self.ent_max.pack(side="left", padx=5)
        add_context_menu(self.ent_max)
        ctk.CTkLabel(time_frame, text=":محدوده تاخیر تصادفی", font=FONT_NORMAL).pack(side="left", padx=10)

        # AI Variation
        ctk.CTkLabel(main_card, text="🧠 تنوع پیام هوشمند", font=FONT_TITLE, text_color=THEME["secondary"]).pack(anchor="e", padx=30, pady=(20, 10))
        
        self.var_ai_enable = ctk.BooleanVar(value=config.get("ai_variation_enabled", False))
        ctk.CTkSwitch(main_card, text="فعال‌سازی بازنویسی هوشمند (ضد اسپم)", variable=self.var_ai_enable, font=FONT_NORMAL).pack(anchor="e", padx=30)
        
        count_frame = ctk.CTkFrame(main_card, fg_color="transparent")
        count_frame.pack(fill="x", padx=30, pady=10)
        self.slider_count = ctk.CTkSlider(count_frame, from_=5, to=50, number_of_steps=45)
        self.slider_count.pack(side="left", fill="x", expand=True)
        self.slider_count.set(config.get("ai_variation_count", 20))
        self.lbl_count = ctk.CTkLabel(count_frame, text=f"{int(self.slider_count.get())}")
        self.lbl_count.pack(side="left", padx=10)
        self.slider_count.configure(command=lambda v: self.lbl_count.configure(text=f"{int(v)}"))
        ctk.CTkLabel(count_frame, text=":تعداد تنوع", font=FONT_NORMAL).pack(side="left")

        ctk.CTkButton(self, text="💾 ذخیره تنظیمات", font=FONT_TITLE, height=50, fg_color=THEME["success"], command=self.save_settings).pack(fill="x", padx=100, pady=40, side="bottom")

    def save_settings(self):
        try:
            d_min = int(self.ent_min.get())
            d_max = int(self.ent_max.get())
            if d_min >= d_max:
                messagebox.showerror("خطا", "حداقل تاخیر باید کمتر از حداکثر باشد.")
                return
            new_config = {
                "delay_min": d_min,
                "delay_max": d_max,
                "ai_variation_enabled": self.var_ai_enable.get(),
                "ai_variation_count": int(self.slider_count.get())
            }
            AIBrain.DATA["bot_config"] = new_config
            AIBrain.save()
            messagebox.showinfo("موفق", "تنظیمات ذخیره شد.")
        except:
            messagebox.showerror("خطا", "مقادیر نامعتبر است.")

# =================================================================
#                  MODULE: ROBOTS HUB (ADDED MISSING CLASS)
# =================================================================
class RobotsHubFrame(ctk.CTkFrame):
    def __init__(self, master, controller):
        super().__init__(master, fg_color=THEME["bg_root"])
        self.controller = controller
        self.setup_ui()

    def setup_ui(self):
        # Header
        head = ctk.CTkFrame(self, fg_color="transparent")
        head.pack(fill="x", padx=30, pady=30)
        ctk.CTkLabel(head, text="🤖 هاب ربات‌های هوشمند", font=(APP_FONT, 20, "bold"), text_color=THEME["primary"]).pack(side="right")
        ctk.CTkLabel(head, text="انتخاب ربات جهت استخراج اطلاعات", font=(APP_FONT, 12), text_color="gray").pack(side="right", padx=10)


        # نوار تنظیمات اتصال به وب‌سایت
        sync_bar = ctk.CTkFrame(self, fg_color=THEME["bg_card"], border_color=THEME["primary"], border_width=1, corner_radius=12)
        sync_bar.pack(fill="x", padx=30, pady=(0, 15))
        
        ctk.CTkLabel(sync_bar, text="🌐 توکن اتصال همگام‌سازی به وب‌سایت:", font=(APP_FONT, 11, "bold"), text_color="white").pack(side="right", padx=15, pady=10)
        
        self.ent_cloud_token = ctk.CTkEntry(sync_bar, placeholder_text="توکن اختصاصی حساب کاربری را اینجا پیست کنید...", font=("Consolas", 11), height=35)
        self.ent_cloud_token.pack(side="right", fill="x", expand=True, padx=10, pady=10)
        if CloudSyncManager.API_TOKEN:
            self.ent_cloud_token.insert(0, CloudSyncManager.API_TOKEN)
        add_context_menu(self.ent_cloud_token)
            
        def _save_sync_token():
            tok = self.ent_cloud_token.get().strip()
            CloudSyncManager.set_config("http://127.0.0.1:8000", tok, True)
            messagebox.showinfo("موفقیت", "توکن همگام‌سازی ذخیره شد. داده‌های استخراج شده مستقیماً به پنل وب شما ارسال خواهند شد.")

        ctk.CTkButton(sync_bar, text="💾 ثبت توکن", fg_color=THEME["secondary"], width=100, height=35, font=(APP_FONT, 11, "bold"), command=_save_sync_token).pack(side="left", padx=15, pady=10)

        # Scrollable Container
        scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Configure Grid (4 Columns for large screens)
        scroll.grid_columnconfigure((0, 1, 2, 3), weight=1)

        bots = [
            {"id": "instagram", "db_id": 1, "name": "اینستاگرام پرو", "icon": "📸", "desc": "استخراج شماره از بایو و کپشن (موتور V21)", "color": THEME["instagram"]},
            {"id": "divar", "db_id": 2, "name": "دیوار منشی", "icon": "🧱", "desc": "جمع‌آوری آگهی‌های هدفمند دیوار", "color": THEME["danger"]},
            {"id": "sheypoor", "db_id": 3, "name": "شیپور پلاس", "icon": "🎺", "desc": "اسکرپر سریع شیپور با شماره", "color": THEME["info"]},
            {"id": "torob", "db_id": 4, "name": "ترب", "icon": "🛍️", "desc": "استخراج فروشگاه‌های اینترنتی", "color": "#D32F2F"},
            {"id": "buskool", "db_id": 5, "name": "باسکول", "icon": "🌾", "desc": "محصولات عمده و کشاورزی", "color": "#FFA000"},
            {"id": "neshan", "db_id": 6, "name": "نقشه نشان", "icon": "📍", "desc": "مشاغل بر اساس لوکیشن", "color": "#1976D2"},
            {"id": "maps", "db_id": 7, "name": "گوگل مپس", "icon": "🗺️", "desc": "دیتای جهانی گوگل مپس", "color": "#388E3C"},
            {"id": "niazrooz", "db_id": 8, "name": "نیاز روز", "icon": "📰", "desc": "نیازمندی‌های سراسری", "color": "#7B1FA2"},
            {"id": "avval", "db_id": 9, "name": "کتاب اول", "icon": "📖", "desc": "بانک مشاغل شهری", "color": "#FBC02D"},
            {"id": "irantejarat", "db_id": 10, "name": "ایران تجارت", "icon": "🏭", "desc": "آگهی‌های صنعتی B2B", "color": "#0288D1"},
        ]

        row = 0
        col = 3 # Start from right (RTL visual)
        
        for bot in bots:
            self.create_bot_card(scroll, bot, row, col)
            col -= 1
            if col < 0:
                col = 3
                row += 1

    def create_bot_card(self, parent, bot, r, c):
        card = ctk.CTkFrame(parent, fg_color=THEME["bg_card"], border_color=THEME["border"], border_width=1)
        card.grid(row=r, column=c, padx=10, pady=10, sticky="nsew")
        
        # Icon
        ctk.CTkLabel(card, text=bot["icon"], font=("Emoji", 40)).pack(pady=(20, 10))
        
        # Title
        ctk.CTkLabel(card, text=bot["name"], font=(APP_FONT, 14, "bold"), text_color="white").pack()
        
        # Desc
        ctk.CTkLabel(card, text=bot["desc"], font=(APP_FONT, 11), text_color="gray", wraplength=180).pack(pady=(5, 15))
        
        # بررسی وضعیت خرید ربات
        purchased_bots = LicenseManager.USER_CONTEXT.get("purchased_bots", [])
        is_unlocked = bot["db_id"] in purchased_bots
        
        # اگر لایسنس کلا غیرفعال باشد، همه قفل می‌شوند
        if not LicenseManager.USER_CONTEXT.get("is_active"):
            is_unlocked = False

        if is_unlocked:
            btn_text = "اجرا"
            btn_color = bot["color"]
            cmd = lambda: self.controller.show_frame(bot["id"])
        else:
            btn_text = "🔒 خرید ماژول"
            btn_color = THEME["bg_input"]
            cmd = lambda b_name=bot["name"]: self.show_locked_msg(b_name)

        # Button
        ctk.CTkButton(card, text=btn_text, fg_color=btn_color, height=35, font=(APP_FONT, 12, "bold"),
                      command=cmd).pack(pady=(0, 20), padx=30, fill="x")

    def show_locked_msg(self, bot_name):
        msg = f"شما هنوز ماژول «{bot_name}» را خریداری نکرده‌اید.\n\nبرای فعالسازی دائمی این ربات روی لایسنس خود، لطفاً به مارکت وب‌سایت مراجعه کنید."
        if messagebox.askyesno("خرید ماژول", f"{msg}\n\nآیا مایلید به فروشگاه هدایت شوید؟"):
            webbrowser.open("https://winboots.ir/user.php?page=market")

# =================================================================
#                  MODULE: DASHBOARD (FIXED & UNIQUE)
# =================================================================
class DashboardProFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=THEME["bg_root"])
        self.build_ui()

    def build_ui(self):
        # Header
        head = ctk.CTkFrame(self, fg_color="transparent")
        head.pack(fill="x", padx=20, pady=20)
        ctk.CTkLabel(head, text="داشبورد مدیریتی (PRO)", font=FONT_HEADER, text_color=THEME["primary"]).pack(side="right")
        ctk.CTkButton(head, text="🔄 بروزرسانی", width=120, command=self.refresh_data, fg_color=THEME["info"], font=(APP_FONT, 12, "bold")).pack(side="left")

        # Stats Cards
        self.cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.cards_frame.pack(fill="x", padx=10, pady=10)
        
        self.lbl_total = self.create_card(self.cards_frame, "کل دیتای استخراج شده", "0", THEME["primary"])
        self.lbl_today = self.create_card(self.cards_frame, "استخراج امروز", "0", THEME["success"])
        self.lbl_bots = self.create_card(self.cards_frame, "ربات‌های فعال", "9", THEME["warning"])
        self.lbl_msgs = self.create_card(self.cards_frame, "پیام‌های ارسالی", "0", THEME["secondary"])

        # Split Content Area (Chart + Announcements)
        split_frame = ctk.CTkFrame(self, fg_color="transparent")
        split_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Configure Grid: 2 Columns
        split_frame.columnconfigure(0, weight=1) # Left (Chart)
        split_frame.columnconfigure(1, weight=1) # Right (Announcements)
        
        # --- Left Side: Chart ---
        chart_container = ctk.CTkFrame(split_frame, fg_color=THEME["bg_card"], corner_radius=15)
        chart_container.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        
        if DATA_ANALYSIS_AVAILABLE:
            self.figure = Figure(figsize=(5, 4), dpi=100, facecolor=THEME["bg_card"])
            self.ax = self.figure.add_subplot(111)
            self.ax.set_facecolor(THEME["chart_bg"])
            self.canvas = FigureCanvasTkAgg(self.figure, master=chart_container)
            self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)
        else:
            ctk.CTkLabel(chart_container, text="ماژول نمودار فعال نیست", text_color="gray").pack(expand=True)

        # --- Right Side: Announcements ---
        ann_container = ctk.CTkFrame(split_frame, fg_color=THEME["bg_card"], corner_radius=15)
        ann_container.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        
        ctk.CTkLabel(ann_container, text="📢 تابلو اعلانات (آنلاین)", font=(APP_FONT, 16, "bold"), text_color=THEME["info"]).pack(pady=15)
        
        self.ann_scroll = ctk.CTkScrollableFrame(ann_container, fg_color="transparent")
        self.ann_scroll.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.refresh_data()

    def create_card(self, parent, title, value, color):
        card = ctk.CTkFrame(parent, fg_color=THEME["bg_card"], border_color=color, border_width=2)
        card.pack(side="right", expand=True, fill="both", padx=10)
        ctk.CTkLabel(card, text=title, font=FONT_NORMAL, text_color=THEME["text_dim"]).pack(pady=(15, 5))
        lbl = ctk.CTkLabel(card, text=value, font=("vazir", 28, "bold"), text_color="white")
        lbl.pack(pady=(0, 15))
        return lbl

    def refresh_data(self):
        # Stats
        stats = DatabaseHandler.get_dashboard_stats()
        self.lbl_total.configure(text=str(stats.get('total', 0)))
        self.lbl_today.configure(text=str(stats.get('today', 0)))
        logs = DatabaseHandler.get_message_logs()
        self.lbl_msgs.configure(text=str(len(logs)))

        # Chart
        if DATA_ANALYSIS_AVAILABLE:
            self.ax.clear()
            bots = ['Divar', 'Sheypoor', 'Neshan', 'Buskool', 'Insta']
            counts = [stats.get(b.lower().replace("insta", "instagram"), 0) for b in bots]
            
            # اصلاح فونت برای نمودار داشبورد
            bots_fa = [PersianTextFixer.fix(b) for b in bots]
            
            bars = self.ax.bar(bots_fa, counts, color=[THEME["primary"], THEME["secondary"], THEME["info"], THEME["warning"], THEME["instagram"]])
            self.ax.set_title(PersianTextFixer.fix("آمار استخراج"), color="white", fontname=APP_FONT)
            self.ax.tick_params(axis='x', colors='white', labelsize=8)
            self.ax.tick_params(axis='y', colors='white')
            for bar in bars:
                height = bar.get_height()
                self.ax.text(bar.get_x() + bar.get_width()/2., height, f'{int(height)}', ha='center', va='bottom', color='white')
            self.canvas.draw()
            
        # Announcements (Thread-Safe)
        threading.Thread(target=self._load_announcements, daemon=True).start()

    def _load_announcements(self):
        # Clear old
        for widget in self.ann_scroll.winfo_children():
            widget.destroy()
            
        data = LicenseManager.fetch_announcements()
        
        if not data:
            ctk.CTkLabel(self.ann_scroll, text="هیچ اطلاعیه‌ای موجود نیست.", text_color="gray", font=FONT_SMALL).pack(pady=20)
            return

        for item in data:
            card = ctk.CTkFrame(self.ann_scroll, fg_color=THEME["bg_input"], corner_radius=8)
            card.pack(fill="x", pady=5)
            
            title_txt = item.get('title', 'بدون عنوان')
            msg_txt = item.get('content', '') or item.get('message', '') 
            date_txt = str(item.get('created_at', ''))[:10]
            
            # Title Row
            t_row = ctk.CTkFrame(card, fg_color="transparent")
            t_row.pack(fill="x", padx=10, pady=(10, 5))
            ctk.CTkLabel(t_row, text=title_txt, font=(APP_FONT, 13, "bold"), text_color="white").pack(side="right")
            ctk.CTkLabel(t_row, text=date_txt, font=("vazir", 10), text_color="gray").pack(side="left")
            
            # Message Body
            ctk.CTkLabel(card, text=msg_txt, font=(APP_FONT, 12), text_color="#DDD", wraplength=350, justify="right").pack(fill="x", padx=10, pady=(0, 10))

# =================================================================
#                  MODULE: REPORTS FRAME (FIXED & PREMIUM)
# =================================================================
class ReportsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=THEME["bg_root"])
        self.build_ui()
    
    def build_ui(self):
        # --- Header ---
        head = ctk.CTkFrame(self, fg_color="transparent")
        head.pack(fill="x", padx=30, pady=20)
        
        ctk.CTkButton(head, text="🔄 بروزرسانی تحلیل‌ها", width=140, height=40, 
                      fg_color=THEME["primary"], hover_color=THEME["primary_hover"],
                      font=(APP_FONT, 13, "bold"), command=self.refresh_analytics).pack(side="left")

        title_frame = ctk.CTkFrame(head, fg_color="transparent")
        title_frame.pack(side="right")
        ctk.CTkLabel(title_frame, text="📊 داشبورد هوش تجاری و تحلیل عملکرد", font=(APP_FONT, 24, "bold"), text_color="white").pack(anchor="e")
        ctk.CTkLabel(title_frame, text="گزارش‌گیری زنده و آنالیز عمیق داده‌های استخراجی و کمپین‌های تبلیغاتی", font=(APP_FONT, 12), text_color="gray").pack(anchor="e")
        
        # --- Unified Premium Scrollable Container ---
        self.scroll = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scroll.pack(fill="both", expand=True, padx=20, pady=5)

        # --- Section 1: KPI Cards ---
        kpi_row = ctk.CTkFrame(self.scroll, fg_color="transparent")
        kpi_row.pack(fill="x", pady=(0, 20))
        for i in range(4): kpi_row.grid_columnconfigure(i, weight=1)

        self.val_scraped = ctk.StringVar(value="0")
        self.val_sent = ctk.StringVar(value="0")
        self.val_rate = ctk.StringVar(value="0%")
        self.val_value = ctk.StringVar(value="0 تومان")

        # ساخت کارت‌های درخشان
        self._create_premium_card(kpi_row, "کل دیتای استخراجی", self.val_scraped, "🎯", "#00E676", 3)
        self._create_premium_card(kpi_row, "کل پیام‌های ارسالی", self.val_sent, "🚀", "#29B6F6", 2)
        self._create_premium_card(kpi_row, "نرخ موفقیت ارسال", self.val_rate, "⚡", "#FFCA28", 1)
        self._create_premium_card(kpi_row, "ارزش تخمینی داده‌ها", self.val_value, "💎", "#AB47BC", 0)

        # --- Section 1.5: JALALI PERFORMANCE CALENDAR ---
        cal_container = ctk.CTkFrame(self.scroll, fg_color=THEME["bg_card"], corner_radius=15, border_width=1, border_color=THEME["border"])
        cal_container.pack(fill="x", pady=10)
        
        cal_head = ctk.CTkFrame(cal_container, fg_color="transparent")
        cal_head.pack(fill="x", padx=20, pady=(15, 10))
        
        self.lbl_cal_month = ctk.CTkLabel(cal_head, text="📅 تقویم عملکرد شمسی (ماه جاری)", font=(APP_FONT, 16, "bold"), text_color="white")
        self.lbl_cal_month.pack(side="right")
        
        legend = ctk.CTkFrame(cal_head, fg_color="transparent")
        legend.pack(side="left")
        ctk.CTkLabel(legend, text="استخراج 🎯", font=(APP_FONT, 11, "bold"), text_color="#00E676").pack(side="right", padx=10)
        ctk.CTkLabel(legend, text="ارسال 🚀", font=(APP_FONT, 11, "bold"), text_color="#29B6F6").pack(side="right", padx=10)

        self.cal_grid = ctk.CTkFrame(cal_container, fg_color="transparent")
        self.cal_grid.pack(fill="x", padx=20, pady=(0, 20))
        
        weekdays = ["شنبه", "یکشنبه", "دوشنبه", "سه‌شنبه", "چهارشنبه", "پنج‌شنبه", "جمعه"]
        for i, day in enumerate(weekdays):
            self.cal_grid.grid_columnconfigure(i, weight=1)
            ctk.CTkLabel(self.cal_grid, text=day, font=(APP_FONT, 12, "bold"), text_color=THEME["text_dim"]).grid(row=0, column=i, pady=5)

        self.calendar_cells = {}
        
        if JALALI_AVAILABLE:
            today = jdatetime.date.today()
            first_day = jdatetime.date(today.year, today.month, 1)
            start_weekday = first_day.weekday() # 0 = Shanbeh
            days_in_month = 31 if today.month <= 6 else (30 if today.month <= 11 else (29 if not today.isleap() else 30))
            m_names = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]
            self.lbl_cal_month.configure(text=f"📅 تقویم عملکرد ({m_names[today.month-1]} {today.year})")

            row, col = 1, start_weekday
            for day in range(1, days_in_month + 1):
                cur_j = jdatetime.date(today.year, today.month, day)
                g_str = cur_j.togregorian().strftime("%Y-%m-%d")
                
                cell = ctk.CTkFrame(self.cal_grid, height=75, corner_radius=10, fg_color="#141414", border_width=1, border_color="#252525")
                cell.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")
                cell.grid_propagate(False)
                
                lbl_day = ctk.CTkLabel(cell, text=str(day), font=("vazir", 14, "bold"), text_color="#555")
                lbl_day.pack(anchor="ne", padx=8, pady=2)
                
                lbl_stats = ctk.CTkLabel(cell, text="", font=(APP_FONT, 11, "bold"), text_color="white", justify="center")
                lbl_stats.pack(anchor="center", expand=True)
                
                if cur_j == today:
                    cell.configure(border_color=THEME["primary"], border_width=2)
                    lbl_day.configure(text_color=THEME["primary"])
                    
                self.calendar_cells[g_str] = {"frame": cell, "lbl_stats": lbl_stats, "lbl_day": lbl_day}
                
                col += 1
                if col > 6: col = 0; row += 1
        else:
            ctk.CTkLabel(self.cal_grid, text="ماژول jdatetime برای نمایش تقویم یافت نشد.", text_color="gray").grid(row=1, column=0, columnspan=7, pady=20)

        # --- Section 2: Advanced Charts ---
        chart_row = ctk.CTkFrame(self.scroll, fg_color="transparent")
        chart_row.pack(fill="x", pady=10)
        chart_row.grid_columnconfigure(0, weight=6) # 60% عرض برای نمودار روند
        chart_row.grid_columnconfigure(1, weight=4) # 40% عرض برای نمودار دایره‌ای

        # کانتینر نمودار روند فعالیت (Area Chart)
        self.trend_container = ctk.CTkFrame(chart_row, fg_color=THEME["bg_card"], corner_radius=15, border_width=1, border_color=THEME["border"])
        self.trend_container.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        ctk.CTkLabel(self.trend_container, text="روند فعالیت سیستم (۷ روز اخیر)", font=(APP_FONT, 14, "bold"), text_color="white").pack(anchor="e", padx=20, pady=15)
        self.chart_canvas_frame = ctk.CTkFrame(self.trend_container, fg_color="transparent")
        self.chart_canvas_frame.pack(fill="both", expand=True, padx=10, pady=(0,10))

        # کانتینر نمودار توزیع پلتفرم (Donut Chart)
        self.pie_container = ctk.CTkFrame(chart_row, fg_color=THEME["bg_card"], corner_radius=15, border_width=1, border_color=THEME["border"])
        self.pie_container.grid(row=0, column=1, sticky="nsew", padx=(10, 0))
        ctk.CTkLabel(self.pie_container, text="توزیع پلتفرم‌های ارسال", font=(APP_FONT, 14, "bold"), text_color="white").pack(anchor="e", padx=20, pady=15)
        self.pie_canvas_frame = ctk.CTkFrame(self.pie_container, fg_color="transparent")
        self.pie_canvas_frame.pack(fill="both", expand=True, padx=10, pady=(0,10))

        if DATA_ANALYSIS_AVAILABLE:
            self._setup_matplotlib()
        else:
            ctk.CTkLabel(self.chart_canvas_frame, text="جهت مشاهده نمودار، ماژول‌های matplotlib و pandas الزامی است.", text_color="gray").pack(expand=True)
            ctk.CTkLabel(self.pie_canvas_frame, text="نمودار در دسترس نیست.", text_color="gray").pack(expand=True)

        # --- Section 3: Recent Activity Table ---
        table_container = ctk.CTkFrame(self.scroll, fg_color=THEME["bg_card"], corner_radius=15, border_width=1, border_color=THEME["border"])
        table_container.pack(fill="x", pady=20)
        
        t_head = ctk.CTkFrame(table_container, fg_color="transparent")
        t_head.pack(fill="x", padx=20, pady=15)
        ctk.CTkLabel(t_head, text="ریز فعالیت‌ها و تراکنش‌های اخیر", font=(APP_FONT, 14, "bold"), text_color="white").pack(side="right")
        ctk.CTkButton(t_head, text="📥 خروجی اکسل کامل", fg_color=THEME["success"], width=130, height=32, font=(APP_FONT, 11, "bold"), command=self.export_excel).pack(side="left")

        tree_frame = ctk.CTkFrame(table_container, fg_color="transparent")
        tree_frame.pack(fill="x", padx=15, pady=(0, 15))
        
        cols = ("گیرنده", "پیام", "پلتفرم", "وضعیت", "نوع", "زمان")
        self.tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=8)
        
        headers = {"گیرنده": 110, "پیام": 400, "پلتفرم": 90, "وضعیت": 90, "نوع": 80, "زمان": 130}
        for c in cols: 
            self.tree.heading(c, text=c)
            self.tree.column(c, anchor="center" if c != "پیام" else "e", width=headers.get(c, 100))
        
        # استایل تاریک و جذاب برای جدول
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#141414", foreground="#E0E0E0", fieldbackground="#141414", rowheight=35, font=(APP_FONT, 10), borderwidth=0)
        style.map("Treeview", background=[("selected", THEME["primary"])], foreground=[("selected", "white")])
        style.configure("Treeview.Heading", background="#1E1E1E", foreground=THEME["secondary"], font=(APP_FONT, 11, "bold"), borderwidth=0)
        
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="left", fill="y")
        self.tree.pack(side="right", fill="both", expand=True)

    def _create_premium_card(self, parent, title, var, icon, color, col):
        card = ctk.CTkFrame(parent, fg_color=THEME["bg_card"], corner_radius=15, border_width=1, border_color="#2A2A2A")
        card.grid(row=0, column=col, padx=8, pady=5, sticky="nsew")
        
        # نوار درخشان بالای کارت
        ctk.CTkFrame(card, fg_color=color, height=3, corner_radius=5).pack(fill="x", padx=15, pady=(15, 0))
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="both", expand=True, padx=20, pady=(10, 20))
        
        ctk.CTkLabel(content, text=icon, font=("Emoji", 28)).pack(side="right", padx=(10, 0))
        text_frame = ctk.CTkFrame(content, fg_color="transparent")
        text_frame.pack(side="right", fill="y", expand=True)
        
        ctk.CTkLabel(text_frame, text=title, font=(APP_FONT, 11), text_color="gray").pack(anchor="e")
        ctk.CTkLabel(text_frame, textvariable=var, font=("vazir", 20, "bold"), text_color="white").pack(anchor="e", pady=(2, 0))

    def _setup_matplotlib(self):
        # ساختار خام نمودارها که در رفرش آپدیت می‌شوند
        self.fig_trend = Figure(figsize=(6, 3), dpi=100, facecolor=THEME["bg_card"])
        self.ax_trend = self.fig_trend.add_subplot(111)
        self.canvas_trend = FigureCanvasTkAgg(self.fig_trend, master=self.chart_canvas_frame)
        self.canvas_trend.get_tk_widget().pack(fill="both", expand=True)

        self.fig_pie = Figure(figsize=(4, 3), dpi=100, facecolor=THEME["bg_card"])
        self.ax_pie = self.fig_pie.add_subplot(111)
        self.canvas_pie = FigureCanvasTkAgg(self.fig_pie, master=self.pie_canvas_frame)
        self.canvas_pie.get_tk_widget().pack(fill="both", expand=True)

    def load_data(self):
        self.refresh_analytics()

    def refresh_analytics(self):
        # 1. آپدیت جدول فعالیت‌ها
        for i in self.tree.get_children(): self.tree.delete(i)
        logs = DatabaseHandler.get_message_logs()
        for log in reversed(logs):
            msg_snippet = str(log[1])[:60] + "..." if len(str(log[1])) > 60 else str(log[1])
            vals = (log[0], msg_snippet, log[2], log[3], log[4], str(log[5])[:16])
            self.tree.insert("", "end", values=vals)

        # 2. آپدیت کارت‌های آماری (KPIs)
        stats = DatabaseHandler.get_dashboard_stats()
        daily_data = DatabaseHandler.get_daily_activity_stats(7)
        
        total_scraped = stats.get('total', 0)
        total_sent = len(logs)
        # رفع مشکل شمارش استاتوس‌ها (پشتیبانی از کلمات مختلف)
        success_sent = sum(1 for log in logs if str(log[3]).lower() in ["sent", "موفق", "true", "ok", "success"])
        
        self.val_scraped.set(f"{total_scraped:,}")
        self.val_sent.set(f"{total_sent:,}")
        
        rate = int((success_sent / total_sent * 100)) if total_sent > 0 else 0
        self.val_rate.set(f"{rate}%")
        
        # محاسبه ارزش: هر شماره استخراجی 50ت و هر پیام 200ت ارزش‌گذاری فرضی می‌شود
        est_val = (total_scraped * 50) + (total_sent * 200)
        self.val_value.set(f"{est_val:,} T")

        # آپدیت مقادیر تقویم عملکرد شمسی
        daily_data_cal = DatabaseHandler.get_daily_activity_stats(45) # 45 روز برای اطمینان از پوشش کل ماه شمسی
        if hasattr(self, 'calendar_cells'):
            for g_date_str, cell_data in self.calendar_cells.items():
                stat = daily_data_cal.get(g_date_str)
                frame = cell_data["frame"]
                lbl_stats = cell_data["lbl_stats"]
                lbl_day = cell_data["lbl_day"]
                
                lbl_stats.configure(text="")
                frame.configure(fg_color="#141414", border_color="#252525")
                # بازگرداندن رنگ روز جاری
                if frame.cget("border_width") == 2: frame.configure(border_color=THEME["primary"])
                
                if stat and (stat['scraped'] > 0 or stat['sent'] > 0):
                    scr = stat['scraped']
                    snt = stat['sent']
                    
                    txt = ""
                    if scr > 0: txt += f"{scr} 🎯\n"
                    if snt > 0: txt += f"{snt} 🚀"
                    lbl_stats.configure(text=txt.strip())
                    
                    score = scr + (snt * 2)
                    if score > 500:
                        frame.configure(fg_color="#1A3320", border_color="#00E676")
                        lbl_day.configure(text_color="#00E676")
                    elif score > 100:
                        frame.configure(fg_color="#182A3A", border_color="#29B6F6")
                        lbl_day.configure(text_color="#29B6F6")
                    else:
                        frame.configure(fg_color="#2A1A3A", border_color=THEME["primary"])
                        lbl_day.configure(text_color=THEME["primary"])

        # 3. آپدیت نمودارها
        if DATA_ANALYSIS_AVAILABLE:
            # --- نمودار روند (Area Chart) ---
            self.ax_trend.clear()
            self.ax_trend.set_facecolor(THEME["bg_card"])
            # استایل دادن به حاشیه‌های نمودار
            self.ax_trend.spines['top'].set_visible(False)
            self.ax_trend.spines['right'].set_visible(False)
            self.ax_trend.spines['left'].set_color('#333')
            self.ax_trend.spines['bottom'].set_color('#333')

            dates = sorted(list(daily_data.keys()))[-7:] 
            if not dates: return
            
            scraped_vals = [daily_data[d]['scraped'] for d in dates]
            sent_vals = [daily_data[d]['sent'] for d in dates]
            short_dates = [d[5:] for d in dates]

            x = range(len(dates))
            
            # کشیدن خط و سایه زیر آن (Area) به همراه اصلاح فونت لیبل‌ها
            lbl_extract = PersianTextFixer.fix('استخراج')
            lbl_send = PersianTextFixer.fix('ارسال پیامک/انبوه')
            
            self.ax_trend.plot(x, scraped_vals, color='#00E676', linewidth=3, marker='o', markersize=6, label=lbl_extract)
            self.ax_trend.fill_between(x, scraped_vals, color='#00E676', alpha=0.15)
            
            self.ax_trend.plot(x, sent_vals, color='#29B6F6', linewidth=3, marker='o', markersize=6, label=lbl_send)
            self.ax_trend.fill_between(x, sent_vals, color='#29B6F6', alpha=0.15)

            self.ax_trend.set_xticks(x)
            self.ax_trend.set_xticklabels(short_dates, color="white", fontsize=9)
            self.ax_trend.tick_params(axis='y', colors='gray', labelsize=9)
            self.ax_trend.legend(loc='upper left', prop={'family': APP_FONT, 'size': 9}, facecolor=THEME["bg_card"], labelcolor="white", edgecolor="#333")
            self.ax_trend.grid(color='#222', linestyle='-', linewidth=1, axis='y', alpha=0.5)
            self.fig_trend.tight_layout()
            self.canvas_trend.draw()

            # --- نمودار دونات پلتفرم‌ها (Donut Chart) ---
            self.ax_pie.clear()
            self.ax_pie.set_facecolor(THEME["bg_card"])
            platforms = [log[2] for log in logs]
            if platforms:
                counts = pd.Series(platforms).value_counts()
                colors = [THEME.get(p.lower(), "#9C27B0") for p in counts.index]
                
                # اصلاح فونت دایره
                labels_fa = [PersianTextFixer.fix(p) for p in counts.index]
                
                # طراحی مدرن دونات
                wedges, texts, autotexts = self.ax_pie.pie(
                    counts, labels=None, autopct='%1.0f%%', startangle=90, 
                    colors=colors, pctdistance=0.75,
                    wedgeprops=dict(width=0.4, edgecolor=THEME["bg_card"], linewidth=2)
                )
                
                self.ax_pie.legend(wedges, labels_fa, loc="center", bbox_to_anchor=(0.5, 0.5), 
                                   frameon=False, labelcolor="white", prop={'family': APP_FONT, 'size': 9})
                plt.setp(autotexts, size=9, weight="bold", color="white")
            else:
                self.ax_pie.text(0.5, 0.5, PersianTextFixer.fix('داده‌ای موجود نیست'), horizontalalignment='center', verticalalignment='center', color='gray', fontname=APP_FONT)
            
            self.fig_pie.tight_layout()
            self.canvas_pie.draw()

    def export_excel(self):
        logs = DatabaseHandler.get_message_logs()
        if not logs: 
            messagebox.showinfo("خطا", "داده‌ای برای خروجی وجود ندارد.")
            return
        try:
            df = pd.DataFrame(logs, columns=["گیرنده", "پیام", "پلتفرم", "وضعیت", "نوع", "زمان"])
            path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")])
            if path:
                df.to_excel(path, index=False)
                messagebox.showinfo("موفق", "خروجی اکسل با موفقیت ذخیره شد.")
        except Exception as e:
            messagebox.showerror("خطا در خروجی", str(e))

class SplashScreen(ctk.CTkToplevel):
    def __init__(self, master_app=None):
        super().__init__()
        self.master_app = master_app
        self.title("Loading...")
        
        # تنظیمات پنجره: بدون حاشیه و وسط‌چین
        self.overrideredirect(True)
        width = 550
        height = 320
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.configure(fg_color="#0F0F0F")
        self.attributes('-topmost', True)
        
        self.build_ui()
        self.progress_val = 0
        self.after(50, self.simulate_loading)

    def build_ui(self):
        # Frame اصلی با حاشیه نئونی
        main_frame = ctk.CTkFrame(self, fg_color="#080808", border_width=2, border_color=THEME["primary"], corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        # لوگو
        logo_path = resource_path(os.path.join("assest", "logo.png"))
        if os.path.exists(logo_path):
            try:
                pil_img = Image.open(logo_path)
                my_image = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(110, 110))
                ctk.CTkLabel(main_frame, text="", image=my_image).pack(pady=(40, 10))
            except: pass
        else:
            ctk.CTkLabel(main_frame, text="WINBO", font=("vazir", 45, "bold"), text_color=THEME["primary"]).pack(pady=(50, 10))

        ctk.CTkLabel(main_frame, text="ULTIMATE ENTERPRISE EDITION V24.5", font=("vazir", 13, "bold"), text_color="white").pack()
        
        self.lbl_status = ctk.CTkLabel(main_frame, text="در حال راه‌اندازی هسته هوشمند...", font=("vazir", 11), text_color="gray")
        self.lbl_status.pack(pady=(35, 5))
        
        self.progress_bar = ctk.CTkProgressBar(main_frame, width=450, height=6, progress_color=THEME["secondary"])
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

    def simulate_loading(self):
        # [اصلاح شماره ۹]: بررسی زنده بودن پنجره قبل از اجرای متد after برای جلوگیری از کرش
        if not self.winfo_exists(): return
        
        steps = [
            (0.1, "Initializing Core Modules..."),
            (0.25, "Loading Database Drivers..."),
            (0.45, "Checking License Status..."),
            (0.60, "Connecting to AI Neural Network..."),
            (0.80, "Optimizing User Interface..."),
            (0.95, "Finalizing Setup..."),
            (1.0, "Ready!")
        ]
        
        if self.progress_val < len(steps):
            prog, txt = steps[self.progress_val]
            self.progress_bar.set(prog)
            self.lbl_status.configure(text=txt)
            self.progress_val += 1
            # سرعت لودینگ تصادفی
            self.after(random.randint(300, 700), self.simulate_loading)
        else:
            if self.master_app and self.master_app.winfo_exists():
                self.master_app.deiconify()
            self.destroy()

class LoginWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("WINBO LOGIN - DIAMOND EDITION")
        self.is_destroyed = False # پرچم مدیریت وضعیت پنجره
        
        # --- UPDATE: Set Window Icon (آیکون پنجره) ---
        try:
            icon_path = resource_path(os.path.join("assest", "logo.ico"))
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)
        except: pass
        
        self.geometry("400x600") 
        self.resizable(False, False)
        # اتصال متد امن خروج
        self.protocol("WM_DELETE_WINDOW", self.safe_destroy)
        self._center_window()
        self.build_ui()
        
        # بررسی ورود خودکار با کمی تاخیر
        self.after(1000, self.check_auto_login)

    def safe_destroy(self):
        """متد ایمن برای بستن پنجره و جلوگیری از خطای invalid command"""
        self.is_destroyed = True
        try:
            self.quit()
            self.destroy()
        except: pass

    def _center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"+{x}+{y}")

    def build_ui(self):
        self.configure(fg_color=THEME["bg_root"])
        
        # --- UPDATE: Logo Display Logic ---
        logo_path = resource_path(os.path.join("assest", "logo.png"))
        logo_loaded = False
        
        if os.path.exists(logo_path):
            try:
                pil_img = Image.open(logo_path)
                my_image = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(130, 130))
                ctk.CTkLabel(self, text="", image=my_image).pack(pady=(40, 10))
                logo_loaded = True
            except: pass
            
        if not logo_loaded:
            ctk.CTkLabel(self, text="WINBO", font=("vazir", 40, "bold"), text_color=THEME["primary"]).pack(pady=(60, 10))

        ctk.CTkLabel(self, text="ENTERPRISE AUTOMATION", font=("vazir", 10), text_color="gray").pack(pady=(0, 40))

        # Input
        ctk.CTkLabel(self, text="کلید لایسنس خود را وارد کنید:", font=(APP_FONT, 12)).pack(pady=(0, 5))
        self.ent_key = ctk.CTkEntry(self, placeholder_text="License Key", width=300, height=45, justify="center", font=("vazir", 12))
        self.ent_key.pack(pady=5)
        
        # FIX: افزودن منوی راست کلیک به صورت داخلی و کاملاً مستقل برای جلوگیری از خطای NameError
        try:
            menu = tk.Menu(self.ent_key, tearoff=0, font=("vazir", 10))
            menu.add_command(label="کپی (Copy)", command=lambda: self.ent_key.event_generate("<<Copy>>"))
            menu.add_command(label="پیست (Paste)", command=lambda: self.ent_key.event_generate("<<Paste>>"))
            menu.add_command(label="برش (Cut)", command=lambda: self.ent_key.event_generate("<<Cut>>"))
            def show_menu(event): 
                menu.tk_popup(event.x_root, event.y_root)
            target = self.ent_key._entry if hasattr(self.ent_key, "_entry") else self.ent_key
            target.bind("<Button-3>", show_menu)
        except: pass
        
        # Buttons
        self.btn_login = ctk.CTkButton(self, text="ورود به سامانه", width=300, height=45, fg_color=THEME["secondary"], font=(APP_FONT, 14, "bold"), command=self.do_login)
        self.btn_login.pack(pady=20)
        
        # Status
        self.lbl_status = ctk.CTkLabel(self, text="آماده جهت بررسی...", text_color="gray", font=(APP_FONT, 12))
        self.lbl_status.pack(pady=10)
        
        # Footer
        hwid = get_hwid()
        ctk.CTkLabel(self, text=f"System HWID: {hwid}", text_color="#333", font=("vazir", 9)).pack(side="bottom", pady=10)

    def check_auto_login(self):
        """بررسی وجود لایسنس ذخیره شده و ورود خودکار"""
        if self.is_destroyed: return
        
        try:
            local_key = DatabaseHandler.get_config("license_key")
            
            if local_key and len(local_key) > 5:
                self.lbl_status.configure(text="🔄 بازیابی لایسنس و بررسی...", text_color=THEME["info"])
                self.ent_key.delete(0, "end")
                self.ent_key.insert(0, local_key) 
                self.btn_login.configure(state="disabled", text="⌛ لطفاً صبر کنید...")
                
                threading.Thread(target=self._auto_login_process, args=(local_key,), daemon=True).start()
            else:
                pass
        except Exception as e:
            print(f"Auto Login Init Error: {e}")

    def _auto_login_process(self, key):
        try:
            valid, msg = LicenseManager.validate_online(key, is_auto=True)
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(valid, msg))
        except Exception as e:
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(False, f"خطای سیستمی: {e}"))

    def do_login(self):
        """مدیریت کلیک دکمه ورود"""
        key = self.ent_key.get().strip()
        if not key:
            messagebox.showerror("خطا", "لطفاً کد لایسنس را وارد کنید.")
            return

        self.btn_login.configure(state="disabled", text="⏳ در حال اتصال به سرور...")
        self.lbl_status.configure(text="بررسی اصالت و قفل سخت‌افزاری...", text_color=THEME["info"])
        
        threading.Thread(target=self._login_process, args=(key,), daemon=True).start()

    def _login_process(self, key):
        try:
            valid, msg = LicenseManager.validate_online(key, is_auto=False)
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(valid, msg))
        except Exception as e:
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(False, f"خطای اتصال: {e}"))

    def _finish_login(self, valid, msg):
        # بررسی حیاتی: اگر پنجره بسته شده، هیچ کاری نکن (رفع باگ invalid command)
        if self.is_destroyed or not self.winfo_exists():
            return

        self.btn_login.configure(state="normal", text="ورود به سامانه")
        
        if valid:
            self.lbl_status.configure(text="✅ هویت تایید شد. خوش آمدید.", text_color=THEME["success"])
            self.after(500, self._launch_main_app)
        else:
            self.lbl_status.configure(text="❌ خطا در ورود", text_color=THEME["danger"])
            if "اینترنت" not in msg and "DNS" not in msg:
                messagebox.showerror("خطای لایسنس", msg)
            else:
                self.lbl_status.configure(text=msg[:50]+"...")

    def _launch_main_app(self):
        if not self.is_destroyed:
            self.is_destroyed = True
            try: self.destroy() 
            except: pass
            app = WinboApp()
            app.mainloop()
        else:
            self.lbl_status.configure(text="❌ خطا در ورود", text_color=THEME["danger"])
            # اگر ورود ناموفق بود و به صورت خودکار انجام شده بود، فیلد را پاک نمی‌کنیم تا کاربر ببیند
            if "اینترنت" not in msg:
                messagebox.showerror("خطای لایسنس", msg)

# =================================================================
#                  MAIN APPLICATION CLASS (UPDATED SIDEBAR)
# =================================================================
#                  MODULE 14: ASSET GENERATOR (Missing Class Fix)
# =================================================================
#                  MODULE: WALLET FRAME (PREMIUM UI + AUTO VERIFY)
# =================================================================
class PaymentCallbackHandler(http.server.SimpleHTTPRequestHandler):
    """هندلر اختصاصی برای دریافت نتیجه پرداخت از مرورگر"""
    def do_GET(self):
        if "/verify" in self.path:
            # استخراج پارامترها
            query = urlparse(self.path).query
            params = parse_qs(query)
            authority = params.get('Authority', [''])[0]
            status = params.get('Status', ['NOK'])[0]
            
            # ذخیره نتیجه در متغیر کلاس پدر (WalletFrame)
            if hasattr(self.server, 'callback_func'):
                self.server.callback_func(authority, status)

            # نمایش پیام در مرورگر کاربر
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            # اصلاح شده: استفاده از لیست رشته‌ها برای جلوگیری از خطای سینتکس
            if status == "OK":
                html_parts = [
                    "<html><head><meta charset='utf-8'>",
                    "<style>",
                    "body { font-family: Tahoma, sans-serif; text-align: center; padding-top: 50px; background-color: #f0fdf4; direction: rtl; }",
                    ".box { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: inline-block; }",
                    "h1 { color: #166534; }",
                    "p { color: #374151; font-size: 18px; }",
                    "</style></head>",
                    "<body><div class='box'>",
                    "<h1>پرداخت با موفقیت بررسی شد ✅</h1>",
                    "<p>عملیات بانکی انجام شد. می‌توانید این پنجره را ببندید و به نرم‌افزار بازگردید.</p>",
                    "<script>setTimeout(function(){ window.close(); }, 3000);</script>",
                    "</div></body></html>"
                ]
                html_content = "".join(html_parts)
            else:
                html_parts = [
                    "<html><head><meta charset='utf-8'>",
                    "<style>",
                    "body { font-family: Tahoma, sans-serif; text-align: center; padding-top: 50px; background-color: #fef2f2; direction: rtl; }",
                    ".box { background: white; padding: 40px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); display: inline-block; }",
                    "h1 { color: #991b1b; }",
                    "p { color: #374151; font-size: 18px; }",
                    "</style></head>",
                    "<body><div class='box'>",
                    "<h1>عملیات ناموفق یا لغو شده ❌</h1>",
                    "<p>پرداخت انجام نشد. می‌توانید به نرم‌افزار بازگردید.</p>",
                    "<script>setTimeout(function(){ window.close(); }, 3000);</script>",
                    "</div></body></html>"
                ]
                html_content = "".join(html_parts)
            
            self.wfile.write(html_content.encode('utf-8'))
        else:
            self.send_response(404)

class WalletFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color=THEME["bg_root"])
        self.server_thread = None
        self.httpd = None
        self.pending_amount = 0
        self.build_ui()

    def build_ui(self):
        # --- Header ---
        head = ctk.CTkFrame(self, fg_color="transparent")
        head.pack(fill="x", padx=30, pady=30)
        
        # Title
        title_frame = ctk.CTkFrame(head, fg_color="transparent")
        title_frame.pack(side="right")
        ctk.CTkLabel(title_frame, text="💰 کیف پول دیجیتال", font=(APP_FONT, 28, "bold"), text_color=THEME["primary"]).pack(anchor="e")
        ctk.CTkLabel(title_frame, text="مدیریت موجودی و شارژ حساب (اتصال هوشمند بانکی)", font=(APP_FONT, 13), text_color="gray").pack(anchor="e")
        
        # Refresh Button
        ctk.CTkButton(head, text="🔄 بروزرسانی موجودی", width=150, height=40, font=(APP_FONT, 12, "bold"), 
                      fg_color=THEME["bg_input"], hover_color=THEME["bg_hover"], border_width=1, border_color=THEME["border"],
                      command=self.refresh_wallet).pack(side="left")

        # --- Balance Card (کارت موجودی) ---
        balance_card = ctk.CTkFrame(self, fg_color=THEME["bg_card"], corner_radius=15, border_width=2, border_color=THEME["success"])
        balance_card.pack(fill="x", padx=30, pady=(0, 20))
        
        # Layout inside card
        bal_inner = ctk.CTkFrame(balance_card, fg_color="transparent")
        bal_inner.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Right: Balance Text
        right_bal = ctk.CTkFrame(bal_inner, fg_color="transparent")
        right_bal.pack(side="right")
        ctk.CTkLabel(right_bal, text="موجودی قابل برداشت شما:", font=(APP_FONT, 14), text_color="gray").pack(anchor="e")
        self.lbl_balance = ctk.CTkLabel(right_bal, text="0 تومان", font=(APP_FONT, 45, "bold"), text_color=THEME["success"])
        self.lbl_balance.pack(anchor="e", pady=(5, 0))
        
        # Left: Actions (Deposit)
        left_action = ctk.CTkFrame(bal_inner, fg_color="transparent")
        left_action.pack(side="left", fill="y")
        
        ctk.CTkLabel(left_action, text="افزایش اعتبار (درگاه بانکی):", font=(APP_FONT, 12, "bold")).pack(anchor="w", pady=(0, 5))
        
        input_row = ctk.CTkFrame(left_action, fg_color="transparent")
        input_row.pack(fill="x")
        
        self.ent_amount = ctk.CTkEntry(input_row, placeholder_text="مبلغ (تومان)", width=150, justify="center", font=(APP_FONT, 13), height=35)
        self.ent_amount.pack(side="left", padx=(0, 10))
        add_context_menu(self.ent_amount)
        
        self.btn_charge = ctk.CTkButton(input_row, text="💳 پرداخت امن آنلاین", width=160, height=35,
                                        font=(APP_FONT, 12, "bold"), fg_color="#FFC107", text_color="black", hover_color="#FFB300",
                                        command=self.initiate_payment)
        self.btn_charge.pack(side="left")
        
        # --- Transaction History (تاریخچه) ---
        hist_frame = ctk.CTkFrame(self, fg_color=THEME["bg_card"], corner_radius=15)
        hist_frame.pack(fill="both", expand=True, padx=30, pady=20)
        
        ctk.CTkLabel(hist_frame, text="📜 تاریخچه تراکنش‌ها", font=(APP_FONT, 16, "bold"), text_color="white").pack(anchor="e", padx=20, pady=15)
        
        # Table
        tree_frame = ctk.CTkFrame(hist_frame, fg_color="transparent")
        tree_frame.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
        cols = ("ID", "Type", "Amount", "Description", "Date")
        self.tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=10)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background=THEME["bg_root"], foreground="white", fieldbackground=THEME["bg_root"], rowheight=35, font=(APP_FONT, 11), borderwidth=0)
        style.configure("Treeview.Heading", background=THEME["bg_input"], foreground=THEME["primary"], font=(APP_FONT, 12, "bold"), borderwidth=0)
        style.map("Treeview", background=[("selected", THEME["primary_hover"])])
        
        headers = {"ID": "شناسه", "Type": "نوع تراکنش", "Amount": "مبلغ (تومان)", "Description": "شرح", "Date": "تاریخ"}
        widths = {"ID": 60, "Type": 100, "Amount": 120, "Description": 300, "Date": 150}
        
        for c in cols:
            self.tree.heading(c, text=headers[c])
            self.tree.column(c, width=widths[c], anchor="center" if c != "Description" else "e")
        
        vsb = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="left", fill="y")
        self.tree.pack(side="right", fill="both", expand=True)
        
        self.refresh_wallet()

    def refresh_wallet(self):
        bal = DatabaseHandler.get_wallet_balance()
        self.lbl_balance.configure(text=f"{int(bal):,} تومان")
        
        for i in self.tree.get_children(): self.tree.delete(i)
        
        rows = DatabaseHandler.get_wallet_history()
        for r in rows:
            t_type = "واریز 🟢" if r[1] == "deposit" else "برداشت 🔴"
            amt = f"{int(r[2]):,}"
            self.tree.insert("", "end", values=(r[0], t_type, amt, r[3], r[4]))

    def start_local_listener(self):
        """راه‌اندازی سرور موقت برای شنود بازگشت از بانک"""
        try:
            # اگر سرور قبلی باز است، ببند
            if self.httpd:
                self.httpd.shutdown()
                self.httpd.server_close()
            
            port = ZARINPAL_CONFIG["CALLBACK_PORT"]
            handler = PaymentCallbackHandler
            self.httpd = socketserver.TCPServer(("", port), handler)
            self.httpd.callback_func = self.on_bank_callback  # اتصال تابع بازگشتی
            
            # اجرا در ترد جداگانه
            self.server_thread = threading.Thread(target=self.httpd.serve_forever, daemon=True)
            self.server_thread.start()
            return True
        except Exception as e:
            print(f"Server Error: {e}")
            return False

    def stop_local_listener(self):
        if self.httpd:
            threading.Thread(target=self.httpd.shutdown).start()
            # self.httpd.server_close() # Shutdown handles close usually

    def on_bank_callback(self, authority, status):
        """این تابع وقتی بانک کاربر را برمی‌گرداند صدا زده می‌شود"""
        # توقف سرور چون کارش تمام شده
        self.stop_local_listener()
        
        # ادامه فرآیند در ترد اصلی UI
        self.after(0, lambda: self.finalize_payment_check(authority, status))

    def initiate_payment(self):
        """Step 1: درخواست پرداخت و باز کردن مرورگر"""
        try:
            amount_str = self.ent_amount.get().strip()
            if not amount_str.isdigit():
                messagebox.showerror("خطا", "لطفاً مبلغ را به صورت عدد (تومان) وارد کنید.")
                return
            
            amount_toman = int(amount_str)
            if amount_toman < 1000:
                messagebox.showerror("خطا", "حداقل مبلغ پرداخت ۱۰۰۰ تومان است.")
                return
            
            self.pending_amount = amount_toman
            amount_rial = amount_toman * 10
            
            # 1. استارت سرور لوکال (برای گوش دادن به بازگشت از سایت شما)
            if not self.start_local_listener():
                messagebox.showerror("خطا", "پورت سیستم درگیر است. لطفاً برنامه را ببندید و دوباره باز کنید.")
                return

            # استفاده از آدرس دامنه شما به جای لوکال‌هاست برای ارسال به بانک
            remote_callback = ZARINPAL_CONFIG["CALLBACK_URL"]
            
            data = {
                "merchant_id": ZARINPAL_CONFIG["MERCHANT"],
                "amount": amount_rial,
                "description": "شارژ کیف پول وینبو",
                "callback_url": remote_callback,
                "metadata": {"email": "user@rightechco.com"}
            }
            
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
            self.btn_charge.configure(state="disabled", text="در حال اتصال به بانک...")
            
            threading.Thread(target=self._req_payment_thread, args=(data, headers)).start()

        except ValueError:
            messagebox.showerror("خطا", "مبلغ وارد شده نامعتبر است.")
            self.btn_charge.configure(state="normal", text="💳 پرداخت امن آنلاین")

    def _req_payment_thread(self, data, headers):
        try:
            response = requests.post(ZARINPAL_CONFIG["ZP_API_REQUEST"], json=data, headers=headers, timeout=10)
            result = response.json()
            
            if 'data' in result and result['data'] and result['data']['code'] == 100:
                authority = result['data']['authority']
                payment_url = f"{ZARINPAL_CONFIG['ZP_API_STARTPAY']}{authority}"
                
                # باز کردن مرورگر
                webbrowser.open(payment_url)
                
                # نمایش دیالوگ انتظار (به‌صورت مودال نیست تا بلاک نکند)
                self.after(0, self._show_waiting_status)
            else:
                err_msg = str(result.get('errors', 'Unknown Error'))
                self.after(0, lambda: [
                    messagebox.showerror("خطا درگاه", f"اتصال به درگاه ناموفق بود.\n{err_msg}"),
                    self.btn_charge.configure(state="normal", text="💳 پرداخت امن آنلاین"),
                    self.stop_local_listener()
                ])
        except Exception as e:
            self.after(0, lambda: [
                messagebox.showerror("خطای شبکه", f"عدم ارتباط با درگاه پرداخت:\n{e}"),
                self.btn_charge.configure(state="normal", text="💳 پرداخت امن آنلاین"),
                self.stop_local_listener()
            ])

    def _show_waiting_status(self):
        self.btn_charge.configure(text="⏳ در انتظار تکمیل پرداخت...", fg_color="#E0E0E0", text_color="black")
        # دکمه‌ای برای بررسی دستی هم اضافه می‌کنیم برای اطمینان
        # (اگر سرور لوکال به هر دلیلی کار نکرد)
        # اما فعلا به اتوماتیک اعتماد می‌کنیم

    def finalize_payment_check(self, authority, status):
        """Step 2: تایید نهایی پس از بازگشت مرورگر"""
        if status != "OK":
            messagebox.showerror("لغو پرداخت", "تراکنش توسط کاربر لغو شد یا ناموفق بود.")
            self.btn_charge.configure(state="normal", text="💳 پرداخت امن آنلاین", fg_color="#FFC107")
            return

        amount_rial = self.pending_amount * 10
        data = {
            "merchant_id": ZARINPAL_CONFIG["MERCHANT"],
            "amount": amount_rial,
            "authority": authority
        }
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        
        threading.Thread(target=self._verify_thread, args=(data, headers, self.pending_amount)).start()

    def _verify_thread(self, data, headers, amount_toman):
        try:
            response = requests.post(ZARINPAL_CONFIG["ZP_API_VERIFY"], json=data, headers=headers, timeout=10)
            result = response.json()
            
            if 'data' in result and result['data'] and result['data']['code'] == 100:
                ref_id = result['data']['ref_id']
                DatabaseHandler.add_wallet_transaction("deposit", amount_toman, f"شارژ آنلاین (کد پیگیری: {ref_id})")
                
                self.after(0, lambda: [
                    self.ent_amount.delete(0, "end"),
                    self.refresh_wallet(),
                    self.btn_charge.configure(state="normal", text="💳 پرداخت امن آنلاین", fg_color="#FFC107"),
                    messagebox.showinfo("پرداخت موفق", f"✅ کیف پول با موفقیت شارژ شد.\nمبلغ: {amount_toman:,} تومان\nکد پیگیری: {ref_id}")
                ])
            elif 'data' in result and result['data'] and result['data']['code'] == 101:
                 self.after(0, lambda: [
                     messagebox.showinfo("اطلاع", "این تراکنش قبلاً تایید شده است."),
                     self.btn_charge.configure(state="normal", text="💳 پرداخت امن آنلاین", fg_color="#FFC107")
                 ])
            else:
                self.after(0, lambda: [
                    messagebox.showerror("پرداخت ناموفق", "تراکنش تایید نشد. اگر مبلغی کسر شده، تا ۷۲ ساعت بازخواهد گشت."),
                    self.btn_charge.configure(state="normal", text="💳 پرداخت امن آنلاین", fg_color="#FFC107")
                ])
        except Exception as e:
            self.after(0, lambda: [
                messagebox.showerror("خطا", f"خطا در تایید تراکنش:\n{e}"),
                self.btn_charge.configure(state="normal", text="💳 پرداخت امن آنلاین", fg_color="#FFC107")
            ])

# =================================================================
#                  SCREEN MANAGERS (FIXED ARCHITECTURE)
# =================================================================
# 🔴 تغییر بزرگ: برای جلوگیری از کرش کردن Tkinter، صفحه اسپلش و لاگین
# اکنون از نوع Toplevel هستند تا ریشه اصلی (Root) همیشه زنده بماند.

class SplashScreen(ctk.CTkToplevel):
    def __init__(self, master_app=None):
        super().__init__(master_app) # اتصال به والد اصلی
        self.master_app = master_app
        self.title("Loading...")
        
        # تنظیمات پنجره: بدون حاشیه و وسط‌چین
        self.overrideredirect(True)
        width = 550
        height = 320
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.configure(fg_color="#0F0F0F")
        self.attributes('-topmost', True)
        
        self.build_ui()
        self.progress_val = 0
        self.after(50, self.simulate_loading)

    def build_ui(self):
        # Frame اصلی با حاشیه نئونی
        main_frame = ctk.CTkFrame(self, fg_color="#080808", border_width=2, border_color=THEME["primary"], corner_radius=0)
        main_frame.pack(fill="both", expand=True)

        # لوگو
        logo_path = resource_path(os.path.join("assest", "logo.png"))
        if os.path.exists(logo_path):
            try:
                pil_img = Image.open(logo_path)
                my_image = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(110, 110))
                ctk.CTkLabel(main_frame, text="", image=my_image).pack(pady=(40, 10))
            except: pass
        else:
            ctk.CTkLabel(main_frame, text="WINBO", font=("vazir", 45, "bold"), text_color=THEME["primary"]).pack(pady=(50, 10))

        ctk.CTkLabel(main_frame, text="ULTIMATE ENTERPRISE EDITION V24.5", font=("vazir", 13, "bold"), text_color="white").pack()
        
        self.lbl_status = ctk.CTkLabel(main_frame, text="در حال راه‌اندازی هسته هوشمند...", font=("vazir", 11), text_color="gray")
        self.lbl_status.pack(pady=(35, 5))
        
        self.progress_bar = ctk.CTkProgressBar(main_frame, width=450, height=6, progress_color=THEME["secondary"])
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

    def simulate_loading(self):
        # بررسی زنده بودن پنجره قبل از اجرای متد after برای جلوگیری از کرش
        if not self.winfo_exists(): return
        
        steps = [
            (0.1, "Initializing Core Modules..."),
            (0.25, "Loading Database Drivers..."),
            (0.45, "Checking License Status..."),
            (0.60, "Connecting to AI Neural Network..."),
            (0.80, "Optimizing User Interface..."),
            (0.95, "Finalizing Setup..."),
            (1.0, "Ready!")
        ]
        
        if self.progress_val < len(steps):
            prog, txt = steps[self.progress_val]
            self.progress_bar.set(prog)
            self.lbl_status.configure(text=txt)
            self.progress_val += 1
            # سرعت لودینگ تصادفی
            self.after(random.randint(300, 700), self.simulate_loading)
        else:
            if self.master_app and self.master_app.winfo_exists():
                self.master_app.deiconify() # نمایش فرم لاگین
            self.destroy()

class LoginWindow(ctk.CTkToplevel):
    def __init__(self, master_app=None):
        super().__init__(master_app)
        global active_login_window
        active_login_window = self # ثبت ارجاع فعال
        
        self.master_app = master_app
        self.title("WINBO LOGIN - DIAMOND EDITION")
        self.is_destroyed = False
        
        try:
            icon_path = resource_path(os.path.join("assest", "logo.ico"))
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)
        except: pass
        
        self.geometry("400x600") 
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.safe_destroy)
        self._center_window()
        self.build_ui()
        
        self.after(500, self.check_auto_login)

    def safe_destroy(self):
        """متد ایمن برای بستن پنجره و جلوگیری از خطای invalid command"""
        self.is_destroyed = True
        try:
            self.quit()
            self.destroy()
        except: pass

    def auto_login_from_web(self, token):
        """فراخوانی از سرور پل محلی به محض دریافت توکن از مرورگر وب"""
        if self.is_destroyed: return
        print(f"⚡ [Auto Login] Automatically verifying web token: {token[:10]}...")
        self.after(0, lambda: [
            self.ent_key.delete(0, "end"),
            self.ent_key.insert(0, token),
            self.do_login()
        ])

    def check_auto_login(self):
        if self.is_destroyed or not self.winfo_exists(): return
        try:
            # ۱. چک کردن دیپ‌لینک مرورگر یا توکن تنظیم‌شده در CloudSyncManager
            target_key = CloudSyncManager.API_TOKEN or DatabaseHandler.get_config("license_key")
            
            if target_key and len(target_key) > 5:
                self.lbl_status.configure(text="🔄 بازیابی توکن و ورود خودکار...", text_color=THEME["info"])
                self.ent_key.delete(0, "end")
                self.ent_key.insert(0, target_key) 
                self.btn_login.configure(state="disabled", text="⌛ لطفاً صبر کنید...")
                threading.Thread(target=self._auto_login_process, args=(target_key,), daemon=True).start()
        except: pass

    def _center_window(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"+{x}+{y}")

    def build_ui(self):
        self.configure(fg_color=THEME["bg_root"])
        
        logo_path = resource_path(os.path.join("assest", "logo.png"))
        logo_loaded = False
        if os.path.exists(logo_path):
            try:
                pil_img = Image.open(logo_path)
                my_image = ctk.CTkImage(light_image=pil_img, dark_image=pil_img, size=(130, 130))
                ctk.CTkLabel(self, text="", image=my_image).pack(pady=(40, 10))
                logo_loaded = True
            except: pass
            
        if not logo_loaded:
            ctk.CTkLabel(self, text="WINBO", font=("vazir", 40, "bold"), text_color=THEME["primary"]).pack(pady=(60, 10))

        ctk.CTkLabel(self, text="ENTERPRISE AUTOMATION", font=("vazir", 10), text_color="gray").pack(pady=(0, 40))

        ctk.CTkLabel(self, text="کلید لایسنس خود را وارد کنید:", font=(APP_FONT, 12)).pack(pady=(0, 5))
        self.ent_key = ctk.CTkEntry(self, placeholder_text="License Key", width=300, height=45, justify="center", font=("vazir", 12))
        self.ent_key.pack(pady=5)
        
        try:
            menu = tk.Menu(self.ent_key, tearoff=0, font=("vazir", 10))
            menu.add_command(label="کپی (Copy)", command=lambda: self.ent_key.event_generate("<<Copy>>"))
            menu.add_command(label="پیست (Paste)", command=lambda: self.ent_key.event_generate("<<Paste>>"))
            menu.add_command(label="برش (Cut)", command=lambda: self.ent_key.event_generate("<<Cut>>"))
            def show_menu(event): 
                menu.tk_popup(event.x_root, event.y_root)
            target = self.ent_key._entry if hasattr(self.ent_key, "_entry") else self.ent_key
            target.bind("<Button-3>", show_menu)
        except: pass
        
        self.btn_login = ctk.CTkButton(self, text="ورود به سامانه", width=300, height=45, fg_color=THEME["secondary"], font=(APP_FONT, 14, "bold"), command=self.do_login)
        self.btn_login.pack(pady=20)
        
        self.lbl_status = ctk.CTkLabel(self, text="آماده جهت بررسی...", text_color="gray", font=(APP_FONT, 12))
        self.lbl_status.pack(pady=10)
        
        hwid = get_hwid()
        ctk.CTkLabel(self, text=f"System HWID: {hwid}", text_color="#333", font=("vazir", 9)).pack(side="bottom", pady=10)

    def check_auto_login(self):
        if self.is_destroyed or not self.winfo_exists(): return
        try:
            local_key = DatabaseHandler.get_config("license_key")
            if local_key and len(local_key) > 5:
                self.lbl_status.configure(text="🔄 بازیابی لایسنس و بررسی...", text_color=THEME["info"])
                self.ent_key.delete(0, "end")
                self.ent_key.insert(0, local_key) 
                self.btn_login.configure(state="disabled", text="⌛ لطفاً صبر کنید...")
                threading.Thread(target=self._auto_login_process, args=(local_key,), daemon=True).start()
        except: pass

    def _auto_login_process(self, key):
        try:
            valid, msg = LicenseManager.validate_online(key, is_auto=True)
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(valid, msg))
        except Exception as e:
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(False, f"خطای سیستمی: {e}"))

    def do_login(self):
        key = self.ent_key.get().strip()
        if not key:
            messagebox.showerror("خطا", "لطفاً کد لایسنس را وارد کنید.")
            return

        self.btn_login.configure(state="disabled", text="⏳ در حال اتصال به سرور...")
        self.lbl_status.configure(text="بررسی اصالت و قفل سخت‌افزاری...", text_color=THEME["info"])
        threading.Thread(target=self._login_process, args=(key,), daemon=True).start()

    def _login_process(self, key):
        try:
            valid, msg = LicenseManager.validate_online(key, is_auto=False)
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(valid, msg))
        except Exception as e:
            if not self.is_destroyed:
                self.after(0, lambda: self._finish_login(False, f"خطای اتصال: {e}"))

    def _finish_login(self, valid, msg):
        if self.is_destroyed or not self.winfo_exists():
            return

        self.btn_login.configure(state="normal", text="ورود به سامانه")
        
        if valid:
            self.lbl_status.configure(text="✅ هویت تایید شد. خوش آمدید.", text_color=THEME["success"])
            self.after(500, self._launch_main_app)
        else:
            self.lbl_status.configure(text="❌ خطا در ورود", text_color=THEME["danger"])
            if "اینترنت" not in msg and "DNS" not in msg:
                messagebox.showerror("خطای لایسنس", msg)
            else:
                self.lbl_status.configure(text=msg[:50]+"...")

    def _launch_main_app(self):
        if not self.is_destroyed:
            self.is_destroyed = True
            try: self.destroy() 
            except: pass
            
            # نمایش برنامه اصلی و ساخت پویا (Dynamic) هدر بعد از دریافت اطلاعات
            if self.master_app:
                self.master_app.init_ui() 
                self.master_app.deiconify()

# =================================================================
#                  اجرای اصلی برنامه (Main Execution)
# =================================================================
if __name__ == "__main__":
    try:
        # تنظیم DPI برای نمایش با کیفیت در ویندوز (High DPI Fix)
        try:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except: pass

        print("--- SYSTEM STARTUP ---")
        print("1. Initializing Database...")
        DatabaseHandler.initialize()
        
        # بارگذاری تنظیمات همگام‌سازی ابری پس از آماده‌سازی کامل دیتابیس
        CloudSyncManager.load_config()
        
        print("2. Checking directories...")
        for d in DIRS.values():
            if not os.path.exists(d): 
                os.makedirs(d)

        # راه‌اندازی سرور محلی برقراری ارتباط با وب‌سایت
        threading.Thread(target=start_local_bridge_server, daemon=True).start()
        
        print("3. Launching Application Architecture...")
        
        # ریشه (Root) اصلی برنامه
        root_app = WinboApp()
        root_app.withdraw() # مخفی کردن پنجره اصلی تا زمان تایید لاگین
        
        # لاگین به عنوان فرزندِ Root ایجاد می‌شود
        login_window = LoginWindow(master_app=root_app)
        login_window.withdraw() # مخفی کردن لاگین تا اتمام اسپلش اسکرین
        
        # ثبت پروتکل اجرا مستقیم از وب در ویندوز
        register_custom_protocol()
        
        # بررسی ورود از طریق دیپ‌لینک مرورگر (winbo://)
        deeplink_data = parse_deeplink_args()
        if deeplink_data.get("token"):
            tok = deeplink_data.get("token")
            CloudSyncManager.set_config("http://127.0.0.1:8000", tok, True)
            print(f"🔗 برنامه از مرورگر اجرا شد! توکن ست گردید: {tok[:10]}...")

        # اسپلش به عنوان فرزندِ لاگین ایجاد می‌شود
        splash = SplashScreen(master_app=login_window)
        
        # اجرای حلقه اصلی (Mainloop) روی ریشه 
        root_app.mainloop()

    except Exception as e:
        print("\n" + "="*60)
        print(f"❌ CRITICAL ERROR (خطای سیستمی): {e}")
        print("="*60)
        import traceback
        traceback.print_exc()
        if sys.stdin and hasattr(sys.stdin, 'isatty') and sys.stdin.isatty():
            try:
                input("\nPress Enter to exit (اینتر بزنید تا خارج شوید)...")
            except: pass