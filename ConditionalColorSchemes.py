import sublime, sublime_plugin
import re

class CustomColorSchemes( sublime_plugin.EventListener ):

	def on_load( self, view ):

		self.new_ColorScheme = None

		window = view.window()

		try:
			windowVariables = window.extract_variables()
			file     = windowVariables[ "file" ]
			filePath = windowVariables[ "file_path" ]
			fileName = windowVariables[ "file_name" ]
		except( AttributeError, KeyError ) as e :
			return

		settings = sublime.load_settings( "ConditionalColorSchemes.sublime-settings" )
		preferred_ColorScheme_Set    = settings.get( "preferred_ColorScheme_Set", "" )
		include_FileName_In_FilePath = settings.get( "include_FileName_In_FilePath", "" )
		fileName_ColorSchemes        = settings.get( "fileName_ColorSchemes", [] )
		filePath_ColorSchemes        = settings.get( "filePath_ColorSchemes", [] )

		if include_FileName_In_FilePath == True:
			filePath = file

		if preferred_ColorScheme_Set == "filePath_ColorSchemes":
			self.get_Conditional_ColorScheme( fileName, fileName_ColorSchemes )
			self.get_Conditional_ColorScheme( filePath, filePath_ColorSchemes )
		elif preferred_ColorScheme_Set == "fileName_ColorSchemes":
			self.get_Conditional_ColorScheme( filePath, filePath_ColorSchemes )
			self.get_Conditional_ColorScheme( fileName, fileName_ColorSchemes )

		if self.new_ColorScheme != None:
			view.settings().set( "color_scheme", self.new_ColorScheme )

	def get_Conditional_ColorScheme( self, regexSource, colorScheme_Set ):

		for entry in colorScheme_Set:

			regexPattern = entry[ "regexPattern" ]
			colorScheme  = entry[ "colorScheme" ]

			if re.match( regexPattern, regexSource ):
				self.new_ColorScheme  = colorScheme
				break
