/* 
Author: lftroq
Description: Sort arrays using std::sort() in C++ 
*/
#include<bits/stdc++.h>
using namespace std;

// === CONFIG ===
const int N_ARRAY = 10;
const int LENGTH_EACH_ARRAY = 1e6;
const int N_FLOAT = 5;

string INPUT_FILE = "../arrays.txt";
string LOG_FILE = "../time.txt";

// === VALIDATION ===

bool validation(vector<float> &array) {
	for(int i = 1; i < (int)array.size(); i++) {
		if(array[i-1] > array[i]) {
			cerr << "Sort failed at index #" << i << ": \n";
			cerr << "array[" << i-1 << "]: " << array[i-1] << '\n';
			cerr << "array[" << i << "]: " << array[i] << '\n';
			return false;
		}
	}
	return true; 
}

bool validation(vector<int> &array) {
	for(int i = 1; i < (int)array.size(); i++) {
		if(array[i-1] > array[i]) {
			cerr << "Sort failed at index #" << i << ": \n";
			cerr << "array[" << i-1 << "]: " << array[i-1] << '\n';
			cerr << "array[" << i << "]: " << array[i] << '\n';
			return false;
		}
	}
	return true; 
}

int main() {
	// FastIO
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	ifstream input((INPUT_FILE).c_str());
	ofstream output((LOG_FILE).c_str());
	for(int index = 0; index < N_ARRAY; index++) {
		double time;
		if(index < N_FLOAT) { // first N_FLOAT arrays contain floats
			vector<float> array(LENGTH_EACH_ARRAY);
			for(auto &x : array) {
				input >> x;
			}
			clock_t before = clock();
			sort(array.begin(), array.end());
			time = (double)(clock() - before)/CLOCKS_PER_SEC;
			if(!validation(array)) {
				return 0;
			}
		}
		else { // last N_ARRAY - N_FLOAT arrays contain integers
			vector<int> array(LENGTH_EACH_ARRAY);
			for(auto &x : array) {
				input >> x;
			}
			clock_t before = clock();
			sort(array.begin(), array.end());
			time = (double)(clock() - before)/CLOCKS_PER_SEC;
			if(!validation(array)) {
				return 0;
			}
		}
		cerr << "Time taken in #" << index + 1 << " array: " << time << " seconds.\n";
		output << (int)(time * 1000) << ' ';
	}
	input.close();
	output.close();
	return 0;
}
