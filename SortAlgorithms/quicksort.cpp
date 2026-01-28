/* 
Author: lftroq
Description: Sort arrays using merge sort algorithm
Source: This implementaion is referenced from Geeksforgeeks, optimizing by using random pivot instead
*/
#include<bits/stdc++.h>
using namespace std;

// === CONFIG ===
const int N_ARRAY = 10;
const int LENGTH_EACH_ARRAY = 1e6;
const int N_FLOAT = 5;

string INPUT_FILE = "../arrays.txt";
string LOG_FILE = "../time.txt";

mt19937_64 rng(chrono::steady_clock::now().time_since_epoch().count());

int randomRange(int l, int r) { // return random integers in range [l, r]
    return l + rng() % (r - l + 1LL);
}

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

// === QUICK SORT FOR FLOAT ARRAY ===

int partition(vector<float> &array, int left, int right) {
	int rpos = randomRange(left, right);
	swap(array[rpos], array[right]);
	float pivot = array[right];
	// cout << " :::" << pivot << ' ' << left << ' ' << right << endl;
	int i = left - 1;
	for(int j = left; j < right; j++) {
		if(array[j] <= pivot) {
			i++;
			swap(array[i], array[j]);
		}
	}
	i++;
	swap(array[i], array[right]);
	return i;
}

void quickSort(vector<float> &array, int left = 0, int right = -1) {	
	if(right == -1)
		right = (int)array.size() - 1;
	// cout << left << ' ' << right << endl;
	if(left >= right)
		return;
	int pivot = partition(array, left, right);
	quickSort(array, left, pivot - 1);
	quickSort(array, pivot + 1, right);
}

// === QUICK SORT FOR INTEGER ARRAY ===

int partition(vector<int> &array, int left, int right) {
	int rpos = randomRange(left, right);
	swap(array[rpos], array[right]);
	int pivot = array[right];
	// cout << " :::" << pivot << ' ' << left << ' ' << right << endl;
	int i = left - 1;
	for(int j = left; j < right; j++) {
		if(array[j] <= pivot) {
			i++;
			swap(array[i], array[j]);
		}
	}
	i++;
	swap(array[i], array[right]);
	return i;
}

void quickSort(vector<int> &array, int left = 0, int right = -1) {
	if(right == -1)
		right = (int)array.size() - 1;
	if(left >= right)
		return;
	int pivot = partition(array, left, right);
	quickSort(array, left, pivot - 1);
	quickSort(array, pivot + 1, right);
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
			quickSort(array);
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
			quickSort(array);
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