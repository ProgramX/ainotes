import 'package:flutter/material.dart';

void main() {
  runApp(TextEditorApp());
}

class TextEditorApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Text Editor',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: TextEditorScreen(),
    );
  }
}

class TextEditorScreen extends StatefulWidget {
  @override
  _TextEditorScreenState createState() => _TextEditorScreenState();
}

class _TextEditorScreenState extends State<TextEditorScreen> {
  TextEditingController _textEditingController = TextEditingController();
  String _currentText = '';
  int _lineCount = 0;
  int _cursorPosition = 0;

  @override
  void initState() {
    super.initState();
    _textEditingController = TextEditingController();
    _textEditingController.addListener(_updateTextInfo);
  }

  @override
  void dispose() {
    _textEditingController.dispose();
    super.dispose();
  }

  void _updateTextInfo() {
    setState(() {
      _currentText = _textEditingController.text;
      _lineCount = _currentText.split('\n').length;
      _cursorPosition = _textEditingController.selection.baseOffset;
    });
  }

  void _newFile() {
    // Implement the logic for creating a new file here
  }

  void _openFile() {
    // Implement the logic for opening a file here
  }

  void _saveFile() {
    // Implement the logic for saving the file here
  }

  void _openSettings() {
    // Implement the logic for opening settings here
  }

  void _openAbout() {
    // Implement the logic for opening the about page here
  }

  void _exitApp() {
    // Implement the logic for exiting the app here
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Text Editor'),
      ),
      drawer: Drawer(
        child: ListView(
          padding: EdgeInsets.zero,
          children: <Widget>[
            DrawerHeader(
              child: Text('Navigation'),
              decoration: BoxDecoration(
                color: Colors.blue,
              ),
            ),
            ListTile(
              leading: Icon(Icons.add),
              title: Text('New File'),
              onTap: () {
                _newFile();
                Navigator.pop(context);
              },
            ),
            ListTile(
              leading: Icon(Icons.folder_open),
              title: Text('Open File'),
              onTap: () {
                _openFile();
                Navigator.pop(context);
              },
            ),
            ListTile(
              leading: Icon(Icons.save),
              title: Text('Save File'),
              onTap: () {
                _saveFile();
                Navigator.pop(context);
              },
            ),
            ListTile(
              leading: Icon(Icons.settings),
              title: Text('Settings'),
              onTap: () {
                _openSettings();
                Navigator.pop(context);
              },
            ),
            ListTile(
              leading: Icon(Icons.info),
              title: Text('About'),
              onTap: () {
                _openAbout();
                Navigator.pop(context);
              },
            ),
            ListTile(
              leading: Icon(Icons.exit_to_app),
              title: Text('Exit'),
              onTap: () {
                _exitApp();
                Navigator.pop(context);
              },
            ),
          ],
        ),
      ),
      body: Column(
        children: [
          Expanded(
            child: Padding(
              padding: EdgeInsets.all(8.0),
              child: TextField(
                controller: _textEditingController,
                maxLines: null,
                keyboardType: TextInputType.multiline,
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                ),
              ),
            ),
          ),
          Padding(
            padding: EdgeInsets.only(left: 16.0, bottom: 8.0),
            child: Row(
              children: [
                Text('Lines: $_lineCount'),
                SizedBox(width: 16.0),
                Text('Cursor: $_cursorPosition'),
                SizedBox(width: 16.0),
                Text('Characters: ${_currentText.length}'),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
