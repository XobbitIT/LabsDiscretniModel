#!/usr/bin/python

import sys
import re
import string

parent = dict()
rank = dict()

def open_file():
    try:
        return open("l1_2.txt")
    except FileNotFoundError:
        print("Oops! File not exist...")
        exit()

    fileName = sys.argv[1]
    try:
        return open(fileName)
    except FileNotFoundError:
        print("Oops! File not exist...")
        exit()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree


file = open_file()

size = int(file.readline())
vertices = []
for i in range(size): vertices.append(i)

matrix = dict()
edges = []

for line_index, line in enumerate(file):
    for index, node in enumerate(re.split('\s', re.sub('\n', '', line))):
        if line_index == index or node == '0' or (str(index) + ',' + str(line_index)) in matrix: continue
        matrix[str(line_index) + ',' + str(index)] = 1
        edges.append((int(node), line_index, index))

graph = { 'vertices': vertices, 'edges': set(edges) }

min_spanning_tree = sorted(kruskal(graph))

print("Minimum spanning tree:")
tree_weight = 0
for node in min_spanning_tree:
    tree_weight += node[0]
    print(str(node[1]) + '->' + str(node[2]) + '(' + str(node[0]) + ')', end='; ')

print("\n Weight of the minimum spanning tree:", tree_weight)

function postman (arr) { let edgeCount = [];
for (let i = 0; i < arr.length; i++) { edgeCount.push(0);
for (let j = 0; j < arr[i].length; j++) { if(arr[i][j] != 0) edgeCount[i]++;
}
}
console.log(edgeCount);

let oddCount = 0;
for (let i = 0; i < edgeCount.length; i++) { if(edgeCount[i] % 2 != 0) oddCount++;
}

if(oddCount > 2){
console.log("Non-Eulerian graph"); console.log("Duplicating edges");

let oddIndexes = [];


for (let i = 0; i < edgeCount.length; i++) { if(edgeCount[i] % 2 != 0) oddIndexes.push(i);
}
console.log(oddIndexes);

let duplicatePairs = [];

while (oddIndexes.length > 1){ let first = oddIndexes[0];
let second;
for (let i = 1; i < oddIndexes.length; i++) {
if(arr[first][oddIndexes[i]] != 0 && !second) second = oddIndexes[i];
}
if(!second) {
console.log("No Eulerian Cycle and can`t duplicate odd edges"); return 0;
}
else{
console.log(second) oddIndexes.splice(oddIndexes.indexOf(first), 1);
oddIndexes.splice(oddIndexes.indexOf(second), 1); console.log(oddIndexes); duplicatePairs.push([first, second]);
}
}

console.log(duplicatePairs); eulerianPath(arr, duplicatePairs);

}else{
console.log("Eulerian graph"); eulerianPath(arr);
}

function eulerianPath(a, b = []) {

let sum = 0;
for (let i = 0; i < a.length; i++) {
for (let j = 0; j < a[i].length; j++) { sum += a[i][j];
}
}
sum /= 2;
for (let i = 0; i < b.length; i++) { sum += a[b[i][0]][b[i][1]];
}

let stack1 = [0]; let stack2 = [0];

let edgeCount = 2; let limit = 0;
while(edgeCount > 1 && limit < 25){ limit++;

let next = "O";
for (let i = 0; i < a[stack1[stack1.length - 1]].length; i++) { if(a[stack1[stack1.length - 1]][i] != 0 && next == "O") next = i;
//console.log(next);
}

console.log("STACK1 = " + stack1); console.log("STACK2 = " + stack2); if(next == stack2[stack2.length - 1]){
stack2.push(stack1[stack1.length - 1])



let newB = [] let del = 0;
for (let i = 0; i < b.length; i++) {
if(!(b[i][0] == stack1[stack1.length - 2] && b[i][1] == stack1[stack1.length - 1]) && !(b[i][0] == stack1[stack1.length - 1] && b[i][1] == stack1[stack1.length - 2])) newB.push(b[i]);
else {
del++;
}
}
b = [...newB]; if(del == 0){
a[stack1[stack1.length - 1]][next] = 0; a[next][stack1[stack1.length - 1]] = 0;
}

}
else{
stack1.push(next);
console.log(stack1[stack1.length - 1]+ " : " +stack1[stack1.length - 2]);

let newB = [] let del = 0;
for (let i = 0; i < b.length; i++) {
if(!(b[i][0] == stack1[stack1.length - 2] && b[i][1] == stack1[stack1.length - 1]) && !(b[i][0] == stack1[stack1.length - 1] && b[i][1] == stack1[stack1.length - 2])) newB.push(b[i]);
else {
del++;
}
}
b = [...newB]; if(del == 0){
a[stack1[stack1.length - 1]][stack1[stack1.length - 2]] = 0; a[stack1[stack1.length - 2]][stack1[stack1.length - 1]] = 0;
}
}


edgeCount = 0;
for (let i = 0; i < a.length; i++) {
for (let j = 0; j < a[i].length; j++) { if(a[i][j] != 0) edgeCount++;
}
}
edgeCount /= 2; edgeCount += b.length; console.log(edgeCount);
}

console.log(stack1); console.log(stack2);

let result = [...stack2];

for (let i = stack1.length - 1; i >= 0; i--) { result.push(stack1[i]);
}

console.log(result); console.log(sum);

}
}

function commisVoyageur (arr){ console.log(arr);

let arrCopy = arr.map(function(arr1) { return arr1.slice();
});

arr = minColRowDel(arr)[0];
let minRow = minColRowDel(arr)[1]; let minCol = minColRowDel(arr)[2]; console.log(arr);

let minLim = minRow.reduce((a, b) => a + b, 0) + minCol.reduce((a, b) => a + b, 0); console.log (`minLim: ${minLim}`);

let limit = 0;
let banList = [];

while(limit < 20 && banList.length < arr.length * 2){ limit++;

let maxZeroMatrix = maxZeroMatrixCount(arr); console.log(maxZeroMatrix);
let maxZero = { value: 0,
position: [0,0]
}
for (let i = 0; i < maxZeroMatrix.length; i++) {
for (let j = 0; j < maxZeroMatrix[0].length; j++) { if(maxZeroMatrix[i][j] > maxZero.value){
maxZero.value = maxZeroMatrix[i][j]; maxZero.position = [i, j];
}
}
}
console.log(maxZero);


includeResult = include(arr, maxZero.position, banList); console.log(includeResult);
notIncludeResult = notInclude(arr, maxZero.position); console.log(notIncludeResult);

if(includeResult.minLim < notIncludeResult.minLim){ console.log(`\n\nIncluding (${maxZero.position})\n\n`); arr = includeResult.matrix; banList.push(maxZero.position[0], maxZero.position[1]);
}else{
console.log(`\n\nNot including (${maxZero.position})\n\n`); arr = notIncludeResult.matrix;
}

console.log("BanList:" + banList);
}

let result = `Edges: `;
for (let i = 0; i < banList.length-1; i+=2) { const element = banList[i];
result += `${banList[i]}-${banList[i+1]}` if(i != banList.length - 2)result += `, `;

}


console.log(result);

let sum = 0;

for (let i = 0; i < arrCopy.length; i++) {
for (let j = 0; j < arrCopy[i].length; j++) {
for (let k = 0; k < banList.length-1; k+=2) {
if(i == banList[k] && j == banList[k+1]) sum += arrCopy[i][j];
}
}
}

console.log("SUM: " + sum);

let resultCycle = cycleBuilder(banList); console.log(resultCycle);

function minColRowDel (arr){

let tempArr = arr.map(function(arr) { return arr.slice();
});

let minRow = []; let minCol = [];

for (let i = 0; i < tempArr.length; i++) { minRow.push(Infinity);
for (let j = 0; j < tempArr[i].length; j++) {
if(tempArr[i][j] < minRow[i]) minRow[i] = tempArr[i][j];
}
}

console.log(`minRow: ${minRow}`);


for (let i = 0; i < tempArr.length; i++) {
for (let j = 0; j < tempArr[i].length; j++) { tempArr[i][j] -= minRow[i];
}
}

console.log(tempArr);

for (let i = 0; i < tempArr.length; i++) { minCol.push(Infinity);
for (let j = 0; j < tempArr[i].length; j++) {
if(tempArr[j][i] < minCol[i]) minCol[i] = tempArr[j][i];
}
}

console.log(`minCol: ${minCol}`);

for (let i = 0; i < tempArr.length; i++) {
for (let j = 0; j < tempArr[i].length; j++) { tempArr[j][i] -= minCol[i];
}
}

return [tempArr, minRow, minCol];
}

function maxZeroMatrixCount(arr){ let result = [];
for (let i = 0; i < arr.length; i++) { result.push([]);
for (let j = 0; j < arr[i].length; j++) { if(arr[i][j] == 0){
let tempArr = arr.map(function(arr) { return arr.slice();
});
tempArr[i][j] = Infinity; let minRow = Infinity;
for (let k = 0; k < tempArr.length; k++) { if(tempArr[i][k] < minRow) minRow = tempArr[i][k];
}

let minCol = Infinity;
for (let k = 0; k < tempArr.length; k++) { if(tempArr[k][j] < minCol) minCol = tempArr[k][j];
}
result[i].push(minRow + minCol);
console.log(`O(${i};${j}) = ${minRow} + ${minCol} = ${minRow + minCol}`);
}
else result[i].push(0);
}
}
return result;
}

function notInclude(inputArr, position){
let tempArr = inputArr.map(function(arr) { return arr.slice();
});
tempArr[position[0]][position[1]] = Infinity;


console.log("SENDING THIS TO NOT include minColRowDel:"); console.log(tempArr);


let exportArr = minColRowDel(tempArr)[0]; let minRow = minColRowDel(tempArr)[1]; let minCol = minColRowDel(tempArr)[2];

minRow.forEach(function(item, i) { if (item == Infinity) minRow[i] = 0; }); minCol.forEach(function(item, i) { if (item == Infinity) minCol[i] = 0; });

let minLim = minRow.reduce((a, b) => a + b, 0) + minCol.reduce((a, b) => a + b, 0); return {matrix:exportArr, minLim:minLim};
}

function include(inputArr, position, banList){ let tempArr = inputArr.map(function(arr) {
return arr.slice();
});
tempArr[position[1]][position[0]] = Infinity;

for (let i = 0; i < banList.length-1; i+=2) { if(banList[i] == position[0]){
tempArr[banList[i+1]][position[1]] = Infinity; tempArr[position[1]][banList[i+1]] = Infinity;
}
if(banList[i + 1] == position[0]){ tempArr[banList[i]][position[1]] = Infinity; tempArr[position[1]][banList[i]] = Infinity;
}

if(banList[i] == position[1]){ tempArr[banList[i+1]][position[0]] = Infinity; tempArr[position[0]][banList[i+1]] = Infinity;
}
if(banList[i+1] == position[1]){ tempArr[banList[i]][position[0]] = Infinity; tempArr[position[0]][banList[i]] = Infinity;
}
}

for (let i = 0; i < tempArr.length; i++) {
for (let j = 0; j < tempArr[i].length; j++) {
if(i == position[0] || j == position[1]) tempArr[i][j] = Infinity;
}
}

console.log("SENDING THIS TO INCLUDE minColRowDel:"); console.log(tempArr);

let exportArr = minColRowDel(tempArr)[0]; let minRow = minColRowDel(tempArr)[1]; let minCol = minColRowDel(tempArr)[2];

minRow.forEach(function(item, i) { if (item == Infinity) minRow[i] = 0; }); minCol.forEach(function(item, i) { if (item == Infinity) minCol[i] = 0; });

let minLim = minRow.reduce((a, b) => a + b, 0) + minCol.reduce((a, b) => a + b, 0);

if(minRow.every( (val, i, arr) => val === arr[0] ) && minCol.every( (val, i, arr) => val === arr[0] ))
minLim--;



return {matrix:exportArr, minLim:minLim};
}

function cycleBuilder (a) { let result = "Cycle: ";
let resultArr = [a[0], a[1]];

for (let i = 0; i < a.length/2 - 1; i++) {
if(findNext(a,	resultArr[resultArr.length	-	1])	!=	Infinity)	resultArr.push(findNext(a, resultArr[resultArr.length - 1]));
else return "Cycle not found";
}

function findNext(a, b){
for (let i = 0; i < a.length - 1; i+=2) { if(a[i] == b) {
return a[i+1];
}
}
return Infinity;
}

for (let i = 0; i < resultArr.length; i++) { result += `(${resultArr[i]})`;
if(i != resultArr.length - 1) result += " => ";
}

return result;
}
}

function fordFulkerson (iArr) {
let arr = iArr.map(function(arr1) { return arr1.slice();
});

let maxFlow = []; let paths = [];
let limit = 0;
while(pathFinder(arr) && limit < 25){ limit++;

let path = pathFinder(arr); console.log(path);

let minEdge = { coordinates: [], value: Infinity, i: 0
}

for (let i = 0; i < path.length; i++) { if(arr[path[i][0]][path[i][1]] < minEdge.value){
minEdge.coordinates = [path[i][0], path[i][1]]; minEdge.value = arr[path[i][0]][path[i][1]]; minEdge.i = i;
}
}

console.log(minEdge);

for (let i = 0; i < path.length; i++) {
if(i == minEdge.i) arr[path[i][0]][path[i][1]] = 0;
else arr[path[i][0]][path[i][1]] -= minEdge.value;
}


maxFlow.push(minEdge.value); paths.push(path);
}

console.log(...maxFlow); console.log(paths);


function pathFinder (a){ let path = [];
let edgeList = [];
for (let i = 0; i < a.length; i++) {
for (let j = 0; j < a[i].length; j++) {
if(a[i][j] != 0) edgeList.push({coordinates:[i,j], value:a[i][j]});
}
}
console.log(edgeList);

if(edgeList.findIndex(val => val.coordinates[0] == 0) == -1) return 0; path.push(edgeList[edgeList.findIndex(val => val.coordinates[0] == 0)].coordinates);

while(edgeList.findIndex(val => val.coordinates[0] == path[path.length - 1][1]) != -1){ console.log(`Found	next:	${edgeList[edgeList.findIndex(val	=>	val.coordinates[0]	==
path[path.length - 1][1])].coordinates}`);
path.push(edgeList[edgeList.findIndex(val	=>	val.coordinates[0]	==	path[path.length	- 1][1])].coordinates);

edgeList.splice(edgeList.findIndex(val => val.coordinates == path[path.length - 1]), 1); console.log("SPLICED");
console.log(`New edgeList: \n`); console.log(edgeList);
if(edgeList.findIndex(val => val.coordinates[0] == path[path.length - 1][1]) == -1 && path[path.length - 1][1] != a.length - 1){
path.splice(path.length - 1);
}
}

if(path[path.length - 1][1] == a.length - 1) return path; else{
console.log(path); console.log("Not a path");
a[path[path.length - 1][0]][path[path.length - 1][1]] = 0 return pathFinder(a);
}
}

}


