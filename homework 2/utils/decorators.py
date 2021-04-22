import time


def wait(action, exception=Exception, timeout=10, delay_retry=0.5, check_result=False, **kwargs):
    time_start = time.time()
    exception_last = None

    while time.time() - time_start < timeout:
        try:
            result = action(**kwargs)

            if check_result:
                if result:
                    return result

                exception_last = f'action "{action.__name__}" returned "{result}"'

            else:
                return result

        except exception as e:
            exception_last = e

        time.sleep(delay_retry)

    raise TimeoutError(f'timeout of action "{action.__name__}" in {timeout} seconds - {exception_last}')
