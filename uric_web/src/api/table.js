import request from '@/utils/request'

export function getList(params) {
  return request({
    url: 'release/app',
    method: 'get',
    params
  })
}
