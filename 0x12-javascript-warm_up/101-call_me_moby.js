#!/usr/bin/node

exports.callMeMoby = (x, theFunction) => {
  while (x) {
    theFunction();
    x--;
  }
};
