#!/usr/bin/python3
"""Console application entry point"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import cmd
from pathlib import Path
import shlex
from textExtraction.baseExtractor import TextExtractor
from textExtraction.wordExtractor import WordExtractor
from textExtraction.PDFExtractor import PDFExtractor
from textExtraction.powerPointExtractor import PowerPointExtractor
from textExtraction.plainTextExtractor import PlainTextExtractor
from textExtraction.factory import get_extractor  # Import the factory function
from textGeneration.claudeTextGen import detailed, summarized, get_bullet_points
from voiceGeneration.csm.voiceGen import generate_voice

class iCommand(cmd.Cmd):
    """Console for the immersive application"""
    prompt = '(immersiveCommand-console) '

    def do_EOF(self, arg):
        """Exits the console"""
        return True

    def do_quit(self, arg):
        """Quit command to quit the program"""
        return True

    def do_extract(self, arg):
        """
        Extract text from a file
        Usage: extract <input_file> [output_file]
        """
        try:
            # Parse arguments
            args = shlex.split(arg)
            if not args:
                print("Error: Please provide an input file")
                return

            input_file = args[0]
            output_file = args[1] if len(args) > 1 else None

            # Get the appropriate extractor
            extractor = get_extractor(input_file)

            # Extract text
            text = extractor.extract_text()

            # Save or print the text
            if output_file:
                extractor.save_text(output_file, text)
                print(f"Text extracted and saved to {output_file}")
            else:
                with open("temp.txt", "w") as f:
                    extractor.save_text("temp.txt", text)

        except (FileNotFoundError, ValueError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def do_detailed(self, arg):
        """Generate a detailed video of the notes"""
        # Make sure arg is provided
        if not arg:
            print("Error: Please provide an input file")
            return
        self.do_extract(arg)  # Pass the arg to do_extract
        generate_voice(detailed())

    def do_summarized(Self, arg):
        """Generate a summarized video"""
        if not arg:
            print("Error: Please provide an input file")
            return
        Self.do_extract(arg)
        generate_voice(summarized())

    def do_bullets(self, arg):
        """Generate Bullets"""
        if not arg:
            print("Error: Please provide an input file")
            return
        self.do_extract(arg)
        get_bullet_points()

    def help(self):
        """Help message for the extraction"""
        print("\nSupported formats:")
        print("  - Plain text files (.txt)")
        print("  - PDF files (.pdf)")
        print("  - Word documents (.docx)")
        print("  - PowerPoint presentations (.pptx)")

    def emptyline(self):
        """Do nothing on empty line"""
        pass


if __name__ == '__main__':
    iCommand().cmdloop()
