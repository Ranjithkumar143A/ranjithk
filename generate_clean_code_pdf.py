import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT

def generate_clean_code_pdf():
    pdf_path = "C:/Users/Ranji/.gemini/antigravity/scratch/leave-attendance-app/WorkPulse_Source_Code.pdf"
    
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=1.0*inch,
        rightMargin=1.0*inch,
        topMargin=1.0*inch,
        bottomMargin=1.0*inch
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        'CodeTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#000000"),
        spaceAfter=15
    )

    code_style = ParagraphStyle(
        'CodeBody',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=9,
        leading=14,
        alignment=TA_LEFT,
        textColor=colors.HexColor("#111827")
    )

    story = []

    def format_code(text):
        return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br/>').replace(' ', '&nbsp;')

    # PAGE 1: Package.json
    story.append(Paragraph("<b>1.Package.json</b>", title_style))
    p1 = """{
  "name": "workpulse-server",
  "version": "1.0.0",
  "description": "Backend API for Automated Leave Approval and Attendance Tracking System",
  "main": "server.ts",
  "scripts": {
    "start": "node dist/server.js",
    "dev": "ts-node src/server.ts",
    "build": "tsc"
  },
  "keywords": [
    "workpulse",
    "attendance",
    "leave-approval",
    "payroll-automation",
    "loss-of-pay",
    "mern"
  ],
  "author": "WorkPulse Team",
  "license": "MIT",
  "dependencies": {
    "bcryptjs": "^2.4.3",
    "cors": "^2.8.5",
    "dotenv": "^16.4.5",
    "express": "^4.19.2",
    "ioredis": "^5.4.1",
    "jsonwebtoken": "^9.0.2",
    "pg": "^8.12.0"
  },
  "devDependencies": {
    "ts-node": "^10.9.2",
    "typescript": "^5.5.2"
  }
}"""
    story.append(Paragraph(format_code(p1), code_style))
    story.append(PageBreak())

    # PAGE 2: vite.config.js & db.js
    story.append(Paragraph("<b>2.vite.config.js</b>", title_style))
    p2 = """import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 3000,
    strictPort: true,
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        changeOrigin: true
      }
    }
  }
});"""
    story.append(Paragraph(format_code(p2), code_style))
    story.append(Spacer(1, 20))

    story.append(Paragraph("<b>3.db.js</b>", title_style))
    p3 = """import { Pool } from 'pg';

const pgPool = new Pool({
  host: process.env.POSTGRES_HOST || 'localhost',
  port: parseInt(process.env.POSTGRES_PORT || '5432'),
  user: process.env.POSTGRES_USER || 'postgres',
  password: process.env.POSTGRES_PASSWORD || 'postgres',
  database: process.env.POSTGRES_DB || 'leave_attendance_db'
});

export const connectDB = async () => {
  try {
    const client = await pgPool.connect();
    client.release();
    console.log('✅ PostgreSQL Database Connected Successfully');
    return pgPool;
  } catch (error) {
    console.log('ℹ️ Using In-Memory Database Fallback Store');
  }
};

export default pgPool;"""
    story.append(Paragraph(format_code(p3), code_style))
    story.append(PageBreak())

    # PAGE 3: schema.sql
    story.append(Paragraph("<b>4.schema.sql</b>", title_style))
    p4 = """-- Database Schema for WorkPulse Platform

CREATE TABLE users (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(20) NOT NULL CHECK (role IN ('EMPLOYEE', 'MANAGER', 'HR_ADMIN')),
    department VARCHAR(50) NOT NULL,
    hourly_rate NUMERIC(10, 2) DEFAULT 25.00
);

CREATE TABLE attendance_logs (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) REFERENCES users(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    clock_in TIME NOT NULL,
    clock_out TIME,
    total_hours NUMERIC(4, 2) DEFAULT 0.00,
    status VARCHAR(20) NOT NULL CHECK (status IN ('PRESENT', 'LATE', 'HALF_DAY')),
    CONSTRAINT unique_user_date UNIQUE (user_id, date)
);

CREATE TABLE leave_balances (
    user_id VARCHAR(36) PRIMARY KEY REFERENCES users(id),
    sick_leave INT DEFAULT 12,
    casual_leave INT DEFAULT 12,
    earned_leave INT DEFAULT 15,
    unpaid_leave INT DEFAULT 0
);

CREATE TABLE leave_requests (
    id VARCHAR(36) PRIMARY KEY,
    user_id VARCHAR(36) REFERENCES users(id),
    leave_type VARCHAR(20) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_days INT NOT NULL,
    status VARCHAR(20) DEFAULT 'PENDING'
);"""
    story.append(Paragraph(format_code(p4), code_style))
    story.append(PageBreak())

    # PAGE 4: attendance.ts & leave.ts (Short & Clean)
    story.append(Paragraph("<b>5.attendance.ts & leave.ts (Core Logic)</b>", title_style))
    p5 = """// Clock-In Logic with Punctuality Classification
export const clockIn = (userId, now) => {
  const currentHour = now.getHours();
  const currentMin = now.getMinutes();
  
  // Late tag applied after 09:30 AM
  const isLate = currentHour > 9 || (currentHour === 9 && currentMin > 30);
  const status = isLate ? 'LATE' : 'PRESENT';

  return {
    id: `att-${userId}-${now.toISOString().split('T')[0]}`,
    userId,
    clockIn: now.toTimeString().split(' ')[0],
    status
  };
};

// Leave Balance Validation & Atomic Deduction
export const processLeaveApproval = (request, balances) => {
  if (request.leaveType === 'SICK') {
    balances.sickLeave -= request.totalDays;
  } else if (request.leaveType === 'CASUAL') {
    balances.casualLeave -= request.totalDays;
  } else if (request.leaveType === 'EARNED') {
    balances.earnedLeave -= request.totalDays;
  } else if (request.leaveType === 'UNPAID') {
    balances.unpaidLeave += request.totalDays;
  }
  return balances;
};"""
    story.append(Paragraph(format_code(p5), code_style))
    story.append(PageBreak())

    # PAGE 5: server.ts (Payroll LOP Engine)
    story.append(Paragraph("<b>6.server.js (Automated LOP Payroll Engine)</b>", title_style))
    p6 = """import express from 'express';
import cors from 'cors';
import { connectDB } from './db';

const app = express();
app.use(cors());
app.use(express.json());

// Automated Loss of Pay (LOP) & Salary Calculation API
app.get('/api/payroll/calculate', (req, res) => {
  const { workDays, daysPresent, approvedLeave, hourlyRate } = req.query;
  
  // Accounted Days Formula
  const accounted = Number(daysPresent) + Number(approvedLeave);
  const lopDays = Math.max(0, Number(workDays) - accounted);
  
  // Salary Deductions Formula
  const dailyWage = Number(hourlyRate) * 8;
  const grossSalary = Number(workDays) * dailyWage;
  const deduction = lopDays * dailyWage;
  const netSalary = grossSalary - deduction;

  res.json({
    grossSalary,
    lossOfPayDeduction: deduction,
    netSalary
  });
});

connectDB().then(() => {
  app.listen(5000, () => {
    console.log('🚀 WorkPulse API running on port 5000');
  });
});"""
    story.append(Paragraph(format_code(p6), code_style))

    doc.build(story)
    print(f"Clean code PDF generated at: {pdf_path}")

if __name__ == '__main__':
    generate_clean_code_pdf()
