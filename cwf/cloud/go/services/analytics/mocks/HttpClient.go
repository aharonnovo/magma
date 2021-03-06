// Code generated by mockery v1.0.0. DO NOT EDIT.

package mocks

import http "net/http"
import mock "github.com/stretchr/testify/mock"
import url "net/url"

// HttpClient is an autogenerated mock type for the HttpClient type
type HttpClient struct {
	mock.Mock
}

// PostForm provides a mock function with given fields: _a0, data
func (_m *HttpClient) PostForm(_a0 string, data url.Values) (*http.Response, error) {
	ret := _m.Called(_a0, data)

	var r0 *http.Response
	if rf, ok := ret.Get(0).(func(string, url.Values) *http.Response); ok {
		r0 = rf(_a0, data)
	} else {
		if ret.Get(0) != nil {
			r0 = ret.Get(0).(*http.Response)
		}
	}

	var r1 error
	if rf, ok := ret.Get(1).(func(string, url.Values) error); ok {
		r1 = rf(_a0, data)
	} else {
		r1 = ret.Error(1)
	}

	return r0, r1
}
