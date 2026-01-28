/* 
Author: lftroq
Description: Sort arrays using merge sort algorithm
Source: This implementaion is referenced from Geeksforgeeks
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

// === MERGE SORT FOR FLOAT ARRAY ===

void Merge(vector<float> &array, int left, int mid, int right) {
	vector<float> leftArr, rightArr;
	for(int i = left; i <= mid; i++) 
		leftArr.push_back(array[i]); 
	for(int i = mid + 1; i <= right; i++) 
		rightArr.push_back(array[i]); 
	int nL = (int)leftArr.size(), nR = (int)rightArr.size();

	// Two pointers
	int L = 0, R = 0, cur = left;
	while(L < nL && R < nR) {
		if(leftArr[L] < rightArr[R]) {
			array[cur] = leftArr[L];
			L++;
		}
		else {
			array[cur] = rightArr[R];
			R++;
		}
		cur++;
	}
	while(L < nL) {
		array[cur] = leftArr[L];
		L++;
		cur++;
	}
	while(R < nR) {
		array[cur] = rightArr[R];
		R++;
		cur++;
	}
}

void mergeSort(vector<float> &array, int left = 0, int right = -1) {
	if(right == -1) 
		right = array.size() - 1;
	if(left == right) 
		return;
	int mid = (left + right) / 2;
	mergeSort(array, left, mid);
	mergeSort(array, mid + 1, right);

	Merge(array, left, mid, right);
}

// === MERGE SORT FOR INTEGER ARRAY ===

void Merge(vector<int> &array, int left, int mid, int right) {
	vector<int> leftArr, rightArr;
	for(int i = left; i <= mid; i++) 
		leftArr.push_back(array[i]); 
	for(int i = mid + 1; i <= right; i++) 
		rightArr.push_back(array[i]); 
	int nL = (int)leftArr.size(), nR = (int)rightArr.size();

	// Two pointers
	int L = 0, R = 0, cur = left;
	while(L < nL && R < nR) {
		if(leftArr[L] < rightArr[R]) {
			array[cur] = leftArr[L];
			L++;
		}
		else {
			array[cur] = rightArr[R];
			R++;
		}
		cur++;
	}
	while(L < nL) {
		array[cur] = leftArr[L];
		L++;
		cur++;
	}
	while(R < nR) {
		array[cur] = rightArr[R];
		R++;
		cur++;
	}
}

void mergeSort(vector<int> &array, int left = 0, int right = -1) {
	if(right == -1) right = array.size() - 1;
	if(left == right) return;
	int mid = (left + right) / 2;
	mergeSort(array, left, mid);
	mergeSort(array, mid + 1, right);

	Merge(array, left, mid, right);
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
			mergeSort(array);
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
			mergeSort(array);
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