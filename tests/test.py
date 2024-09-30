import time
import os
from funboost import boost, BrokerEnum, BoosterParams, FunctionResultStatusPersistanceConfig
import threading


@boost('queue_test_f03', is_using_rpc_mode=True,
       function_result_status_persistance_conf=FunctionResultStatusPersistanceConfig(
           is_save_status=True, is_save_result=True, expire_seconds=7 * 24 * 3600))
def task_fun(result):
    return result


def show_result(status_and_result):
    print(status_and_result)


if __name__ == "__main__":

    for i in range(300):
        a = task_fun.push(i)
        a.set_callback(show_result)
