
"use strict";

let TestNestedService = require('./TestNestedService.js')
let SendBytes = require('./SendBytes.js')
let TestArrayRequest = require('./TestArrayRequest.js')
let TestResponseOnly = require('./TestResponseOnly.js')
let AddTwoInts = require('./AddTwoInts.js')
let TestRequestAndResponse = require('./TestRequestAndResponse.js')
let TestMultipleResponseFields = require('./TestMultipleResponseFields.js')
let TestRequestOnly = require('./TestRequestOnly.js')
let TestEmpty = require('./TestEmpty.js')
let TestMultipleRequestFields = require('./TestMultipleRequestFields.js')

module.exports = {
  TestNestedService: TestNestedService,
  SendBytes: SendBytes,
  TestArrayRequest: TestArrayRequest,
  TestResponseOnly: TestResponseOnly,
  AddTwoInts: AddTwoInts,
  TestRequestAndResponse: TestRequestAndResponse,
  TestMultipleResponseFields: TestMultipleResponseFields,
  TestRequestOnly: TestRequestOnly,
  TestEmpty: TestEmpty,
  TestMultipleRequestFields: TestMultipleRequestFields,
};
