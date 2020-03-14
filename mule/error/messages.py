#!/usr/bin/env python3

CANNOT_LOCATE_TASK="Could not locate task with name {}\nPlease reference documentation or submit an issue"
CANNOT_LOCATE_TASK_CONFIGS="Task {} listed another task {} as a dependency, but the task configs could not be found"
CANNOT_PARSE_TASK="Could not parse task at index {} of executing stage"
CANNOT_EVALUATE_ENV_VAR="Could not evaluate environment variable {} referenced in cicd yaml file"
TASK_MISSING_REQUIRED_FIELDS="Task {} is missing required field {}.\nThe following fields are required {}"
TASK_FIELD_MISSING="A task is missing its task field"
JOB_NOT_FOUND="Could not find job for name {}"
TASK_DEPENDENCY_CYCLIC_DEPENDENCY="Task {} has requested task {} twice in your job's execution chain\nTask dependencies must be acyclic"
TASK_DEPENDENCY_CHAIN_TIMEOUT="Could not evaluate dependency chain of your job\nAn infinite loop may have been found in your job's task dependencies"
FIELD_NOT_FOUND="Field {} was not found"
FIELD_VALUE_WRONG_TYPE="Field {} is the wrong type, expected {} got {}"
FIELD_VALUE_COULD_NOT_BE_VALIDATED="Value of field {} could not be validated:\n{}"
JOB_CONFIG_WRONG_TYPE="Job {} is the wrong type, expected {} got {}"
JOB_MISSING_REQUIRED_FIELDS="Job {} is missing required fields.\nThe following fields are required {}"
JOB_FIELD_IS_WRONG_TYPE="Job {} has a field {} with the wrong type, expected {} got {}"
MULE_DRIVER_EXCEPTION="Mule could not execute job {} in file {}\n{}\n"
