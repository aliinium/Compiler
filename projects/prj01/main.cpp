#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cctype>

using namespace std;

bool isKeywordChar(char c) {
    return isupper(c) && (c == 'D' || c == 'I' || c == 'T' || c == 'P');
}

bool isKeyword(const string& word) {
    static const string keywords[] = {"dim", "if", "then", "print", "=", "==", "(", ")"};
    for (const string& keyword : keywords) {
        if (keyword == word) {
            return true;
        }
    }
    return false;
}

vector<string> splitCode(const string& input) {
    vector<string> tokens;
    string word;
    bool isKeywordFlag = false;

    for (char c : input) {
        if (isspace(c) || c == '\n' || c == '\t') {
            if (!word.empty()) {
                tokens.push_back(word);
            }
            word.clear();
            isKeywordFlag = false;
        } else {
            if (isKeywordFlag) {
                word += c;
            } else if (isKeywordChar(c) && isupper(c)) {
                word = c;
                isKeywordFlag = isKeyword(word);
            } else {
                word += c;
            }

        }
    }

    if (!word.empty()) {
        tokens.push_back(word);
    }

    return tokens;
}

int main() {
    string fileName = "/Users/aliinium/Desktop/Uni-Assignments/Compiler/projects/prj01/code.txt";

    ifstream inputFile(fileName);
    if (inputFile.is_open()) {
        string line;
        while (getline(inputFile, line)) {
            vector<string> tokens = splitCode(line);
            for (const string& token : tokens) {
                cout << token << endl;
            }
        }
        inputFile.close();
    } else {
        cerr << "Error opening file: " << fileName << endl;
    }

    return 0;
}
