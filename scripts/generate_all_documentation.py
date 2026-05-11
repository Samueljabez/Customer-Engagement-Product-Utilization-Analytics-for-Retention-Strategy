"""
Master script to generate all project documentation PDFs
"""

import os
import sys
import subprocess

print("=" * 80)
print("BANK CHURN ANALYSIS - PDF DOCUMENTATION GENERATOR")
print("=" * 80)

# Change to scripts directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Generate Research Paper
print("\n[1/2] Generating Research Paper PDF...")
try:
    exec(open('generate_research_paper.py').read())
except Exception as e:
    print(f"✗ Error generating research paper: {e}")

# Generate Executive Summary
print("\n[2/2] Generating Executive Summary for Government Stakeholders...")
try:
    exec(open('generate_executive_summary.py').read())
except Exception as e:
    print(f"✗ Error generating executive summary: {e}")

print("\n" + "=" * 80)
print("PDF GENERATION COMPLETE!")
print("=" * 80)

# List generated files
reports_dir = '../reports'
if os.path.exists(reports_dir):
    print(f"\nGenerated files in {reports_dir}:")
    for file in os.listdir(reports_dir):
        file_path = os.path.join(reports_dir, file)
        size = os.path.getsize(file_path) / 1024
        print(f"  • {file} ({size:.1f} KB)")

print("\n✓ All documentation has been successfully generated!")
print("  Access the files in the 'reports/' directory.\n")
