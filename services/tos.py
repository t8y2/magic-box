from core.config import settings
from logger.logger import log
import tos


class TosService(object):

    @classmethod
    def upload(cls, file_uri: str, content: bytes):
        try:
            client = tos.TosClientV2(
                settings.VOLCENGINE_ACCESS,
                settings.VOLCENGINE_SECRET,
                settings.TOS_ENDPOINT,
                settings.TOS_REGION
            )
            result = client.put_object(settings.TOS_BUCKET_NAME, file_uri, content=content)
            log.info(f"Tos {file_uri} upload success")
            return file_uri
        except tos.exceptions.TosClientError as e:
            # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
            log.error('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
        except tos.exceptions.TosServerError as e:
            # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
            log.error('fail with server error, code: {}'.format(e.code))
            # request id 可定位具体问题，强烈建议日志中保存
            log.error('error with request id: {}'.format(e.request_id))
            log.error('error with message: {}'.format(e.message))
            log.error('error with http code: {}'.format(e.status_code))
            log.error('error with ec: {}'.format(e.ec))
            log.error('error with request url: {}'.format(e.request_url))
        except Exception as e:
            log.error('fail with unknown error: {}'.format(e))

        log.info(f"Tos {file_uri} upload failure")

    @classmethod
    def download(cls, file_uri: str):
        try:
            client = tos.TosClientV2(
                settings.VOLCENGINE_ACCESS,
                settings.VOLCENGINE_SECRET,
                settings.TOS_ENDPOINT,
                settings.TOS_REGION
            )
            object_stream = client.get_object(settings.TOS_BUCKET_NAME, file_uri)
            stream = object_stream.read()
            log.info(f"Tos {file_uri} download success")
            return stream
        except tos.exceptions.TosClientError as e:
            # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
            log.error('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
        except tos.exceptions.TosServerError as e:
            # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
            log.error('fail with server error, code: {}'.format(e.code))
            # request id 可定位具体问题，强烈建议日志中保存
            log.error('error with request id: {}'.format(e.request_id))
            log.error('error with message: {}'.format(e.message))
            log.error('error with http code: {}'.format(e.status_code))
            log.error('error with ec: {}'.format(e.ec))
            log.error('error with request url: {}'.format(e.request_url))
        except Exception as e:
            log.error('fail with unknown error: {}'.format(e))

        log.info(f"Tos {file_uri} download failure")
