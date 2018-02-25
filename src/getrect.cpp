#include<iostream>
#include<queue>
#include<vector>
#include<unordered_set>
#include<cassert>
#include <Python.h>

using namespace std;

typedef pair<int, int> ii;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void getIsland(vector<vector<int>> &img, int i, int j, unordered_set<ii> &pts){
    if(img.empty() || img[0].empty()) return;
    int m = (int)img.size(), n = (int)img[0].size();
    queue<ii> Q;
    Q.push(ii(i, j));
    pts.insert(i, j);
    while(!Q.empty()){
        auto r = Q.front();
        Q.pop();
        for(int k=0;k<4;++k){
            int i1 = r.first + dx[k], j1 = r.second + dy[k];
            if(i1>=0 && i1<m && j1>=0 && j1<n && img[i1][j1]==1 && !pts.count(ii(i1, j1))){
                Q.push(ii(i1, j1));
                pts.insert(ii(i1, j1));
            }
        }
    }
    return;
}

vector<vector<int>> getRectangles(vector<vector<int>> img){
    vector<vector<int>> ans;
    if(img.empty() || img[0].empty()) return ans;
    int m = (int)img.size(), n = (int)img[0].size();
    for(int i=0;i<m;++i) for(int j=0;j<n;++j) if(img[i][j] == 1){
        unordered_set<ii> pts;
        getIsland(img, i, j, pts);
        int left, right, top, bottom;
        for(auto p: pts){
            left = min(left, p.second);
            right = max(right, p.second);
            top = min(top, p.first);
            bottom = max(bottom, p.first);
            img[p.first][p.first] = 2;
        }
        ans.push_back(vector<int>{top, left, bottom+1-top, right+1-left});
    }
    return ans;
}
