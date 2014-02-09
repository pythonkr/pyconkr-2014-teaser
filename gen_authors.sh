#!/bin/bash

git shortlog -s -e | cut -c8- > AUTHORS
