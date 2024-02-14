<template>
    <div class="device">
        <a-card size="small" :
                bordered="false">
            <a-row>
                <a-col :span="6">
                    <a-form-item label="单板类别：" :label-col="formItemLayout.labelCol"
                                 :wrapper-col="formItemLayout.wrapperCol">
                        <a-select style="width: 120px;" placeholder="请选择" @change="handleSelectChange"
                                  v-model="device_form.form.category">
                            <a-select-option :value="value.id" v-for="(value, index) in categorys" :key="value.id">
                                {{ value.name }}
                            </a-select-option>
                        </a-select>
                    </a-form-item>
                </a-col>
                <a-col :span="6">
                    <a-form-item :label-col="formItemLayout.labelCol" :wrapper-col="formItemLayout.wrapperCol"
                                 label="单板别名：">
                        <a-input placeholder="请输入"/>
                    </a-form-item>
                </a-col>
                <a-col :span="6">
                    <a-form-item :label-col="formItemLayout.labelCol" :wrapper-col="formItemLayout.wrapperCol"
                                 label="连接地址：">
                        <a-input
                                v-decorator="['nickname', { rules: [{ required: checkdevice, message: 'Please input your nickname' }] }, ]"
                                placeholder="请输入"/>
                    </a-form-item>
                </a-col>
                <a-col :span="6">
                    <router-link to="/workbench">
                        <a-button type="primary" icon="sync" style="margin-top: 3px;">
                            刷新页面
                        </a-button>
                    </router-link>
                </a-col>
            </a-row>

            <div class="add_device" style="margin-bottom: 15px;">
                <a-button type="primary" icon="plus" @click="showModal">
                    新建
                </a-button>
                <a-button type="primary" icon="import" @click="showExcelModal" style="margin-left: 20px;">
                    批量导入
                </a-button>
            </div>
            <!-- 新增单板 -->
            <a-modal
                    :width="800"
                    title="新建单板"
                    :visible="visible"
                    :confirm-loading="confirmLoading"

                    @cancel="handleCancel"
            >
                <template slot="footer">
                    <a-button key="back" @click="handleCancel">取消</a-button>
                    <a-button key="submit" type="primary" :loading="loading" @click="onSubmit">验证</a-button>
                </template>
                <a-form-model ref="ruleForm" :model="device_form.form" :rules="device_form.rules"
                              :label-col="device_form.labelCol" :wrapper-col="device_form.wrapperCol">

                    <a-form-model-item label="单板类别" prop="zone">
                        <a-row>
                            <a-col :span="12">
                                <a-select v-model="device_form.form.category" placeholder="请选择单板类别/区域/分组">
                                    <a-select-option :value="value.id" v-for="(value, index) in categorys"
                                                     :key="value.id">
                                        {{ value.name }}
                                    </a-select-option>
                                </a-select>
                            </a-col>
                            <a-col :span="5" :offset="2">
                                <button type="button" class="ant-btn ant-btn-link" @click="showadddevicecaterage"><span>添加单板类别</span>
                                </button>
                            </a-col>
                            <a-col :span="5">
                                <button type="button" class="ant-btn ant-btn-link"><span>编辑单板类别</span></button>
                            </a-col>
                        </a-row>
                    </a-form-model-item>
                    <a-form-model-item ref="name" label="单板名称" prop="name">
                        <a-row>
                            <a-col :span="24">
                                <a-input placeholder="请输入单板名称" v-model="device_form.form.name"/>
                            </a-col>
                        </a-row>

                    </a-form-model-item>

                    <a-form-model-item ref="ip_addr" label="单板IP地址" prop="ip_addr">
                        <a-row>
                            <a-col :span="24">
                                <a-input placeholder="请输入单板名称" v-model="device_form.form.name"/>
                            </a-col>
                        </a-row>
                    </a-form-model-item>
                    <a-form-model-item ref="pdu_" label="单板IP地址" prop="ip_addr">
                        <a-row>
                            <a-col :span="24">
                                <a-input placeholder="请输入单板名称" v-model="device_form.form.name"/>
                            </a-col>
                        </a-row>
                    </a-form-model-item>

                    <a-form-model-item ref="description" label="备注信息" prop="description">
                        <a-row>
                            <a-col :span="24">
                                <a-textarea v-model="device_form.form.description" placeholder="请输入单板备注信息"
                                            :auto-size="{ minRows: 3, maxRows: 5 }"/>
                            </a-col>
                        </a-row>
                    </a-form-model-item>

                    <a-form-model-item>
                        <a-row>
                            <a-col :span="24" :offset="10">
                  <span>
                    <a-icon type="warning" style="color:yellow;"/>
                    首次验证时需要输入登录用户名对应的密码，但不会存储该密码。
                  </span>
                            </a-col>
                        </a-row>
                    </a-form-model-item>
                </a-form-model>
            </a-modal>
            <a-modal
                    :width="800"
                    title="新建单板类别"
                    :visible="visible_type"
                    :confirm-loading="confirmLoading"

                    @cancel="handleCancel_category"
            >
                <template slot="footer">
                    <a-button key="back" @click="handleCancel_category">取消</a-button>
                    <a-button key="submit" type="primary" :loading="loading" @click="onSubmit_category">确认</a-button>
                </template>
                <a-form-model ref="ruleForm" :model="category_form.form" :rules="category_form.rules"
                              :label-col="category_form.labelCol" :wrapper-col="category_form.wrapperCol">

                    <a-form-model-item label="单板类别" prop="zone">
                    </a-form-model-item>
                    <a-form-model-item ref="name" label="单板类别" prop="name">
                        <a-row>
                            <a-col :span="24">
                                <a-input placeholder="请输入单板类别" v-model="category_form.form.category"/>
                            </a-col>
                        </a-row>
                    </a-form-model-item>
                </a-form-model>
            </a-modal>
            <!-- 批量导入单板 -->
            <div class="excel_push_modal">
                <a-modal v-model="excel_model_visible" title="批量导入单板信息" on-ok="handleUploadExcel" width="800px">
                    <template slot="footer">
                        <a-button key="back" @click="handleUploadExcelCancel">取消</a-button>
                        <a-button type="primary" :disabled="excel_fileList.length === 0" :loading="excel_uploading"
                                  style="margin-top: 16px" @click="handleExcelUpload">
                            {{ excel_uploading ? '上传处理中...' : '开始上传' }}
                        </a-button>
                    </template>
                    <div>
                        <a-alert type="info" message="导入或输入的密码仅作首次验证使用，并不会存储密码。" banner
                                 closable/>
                        <br/>
                        <a-form :form="upload_excel_form">
                            <a-form-item :label-col="formItemLayout.labelCol" :wrapper-col="formItemLayout.wrapperCol"
                                         label="模板下载" help="请下载使用该模板填充数据后导入">
                                <a :href="`${$settings.device}/static/单板导入模板.xls`" download="单板导入模板.xls">单板导入模板.xls</a>
                            </a-form-item>
                            <a-form-item :label-col="formItemLayout.labelCol" :wrapper-col="formItemLayout.wrapperCol"
                                         label="默认密码" help="如果Excel中密码为空则使用该密码">
                                <a-input v-model="default_password" placeholder="请输入默认单板密码"/>
                            </a-form-item>
                            <a-form-item :label-col="formItemLayout.labelCol" :wrapper-col="formItemLayout.wrapperCol"
                                         label="导入数据">
                                <div class="clearfix">
                                    <a-upload :file-list="excel_fileList" :remove="handleExcelRemove"
                                              :before-upload="beforeExcelUpload"
                                              v-decorator="[ 'device_excel', { rules: [{ required: true, message: '请上传文件' }] }, ]">
                                        <a-button>
                                            <a-icon type="upload"/>
                                            选择上传的文件
                                        </a-button>
                                    </a-upload>
                                </div>
                            </a-form-item>
                        </a-form>
                    </div>
                </a-modal>
            </div>
            <!-- 单板列表 -->
            <!-- 单板列表 -->
            <a-table :columns="columns" :data-source="data" rowKey="id">
          <span slot="action" slot-scope="record">
            <a href="javascript:;">编辑</a> |
            <a href="javascript:;">删除</a> |
            <router-link :to="`/uric/console/${record.id}`">Console</router-link>
          </span>
            </a-table>
        </a-card>
    </div>
</template>

<script>
const formItemLayout = {
    labelCol: {span: 8},
    wrapperCol: {span: 12},
};

const columns = [
    {
        title: '类别',
        dataIndex: 'category_name',
        key: 'category_name',
    },
    {
        title: '单板名称',
        dataIndex: 'name',
        key: 'name',
        sorter: true,

    },
    {
        title: '连接地址',
        dataIndex: 'ip_addr',
        key: 'ip_addr',
        ellipsis: true,
        sorter: true,
        width: 200,
    },
    {
        title: 'pdu_ip',
        dataIndex: 'pdu_ip',
        key: 'pdu_ip',
        ellipsis: true,
    },
    {
        title: 'pdu_port',
        dataIndex: 'pdu_port',
        key: 'pdu_port',
        ellipsis: true,
    },

    {
        title: 'sharehost_ip',
        dataIndex: 'sharehost_ip',
        key: 'sharehost_ip',
        ellipsis: true,
    },
    {
        title: 'sharehost_port',
        dataIndex: 'sharehost_port',
        key: 'sharehost_port',
        ellipsis: true,
    },
    {
        title: '备注信息',
        dataIndex: 'description',
        key: 'description',
        ellipsis: true,
    },
];

export default {
    name: "Device",
    data() {
        return {
            loading: false,
            formItemLayout,   // formItemLayout: formItemLayout,
            checkdevice: false, // 是否验证信息
            visible: false,   // 是否显示添加单板的弹窗
            visible_type: false,   // 是否显示添加单板的弹窗
            confirmLoading: false,
            categorys: [     // 单板类别
            ],
            data: [],
            columns: columns, // 表格的表头信息
            // 上传文件的配置参数
            upload_pkey_headers: {
                authorization: 'authorization-text',
            },
            // 添加单板需要的数据属性
            device_form: {
                labelCol: {span: 6},
                wrapperCol: {span: 14},
                other: '',
                form: {
                    name: '',
                    category: '',
                    ip_addr: '',
                    pdu_ip: '',
                    pdu_port: '',
                    sharehost_ip: '',
                    sharehost_port: '',
                    description: '',
                },
                rules: {
                    name: [
                        {required: true, message: '请输入单板名称', trigger: 'blur'},
                        {min: 3, message: '长度在3-20位之间', trigger: 'blur'},
                    ],
                    password: [
                        {required: true, message: '请输入连接密码', trigger: 'blur'},
                        {min: 3, max: 20, message: '长度在3-10位之间', trigger: 'blur'},
                    ],
                    category: [{required: true, message: '请选择类别', trigger: 'change'}],

                    ip_addr: [
                        {required: true, message: '请输入连接地址', trigger: 'blur'},
                        {max: 50, message: '长度最大15位', trigger: 'blur'},
                    ],

                    port: [
                        {required: true, message: '请输入端口号', trigger: 'blur'},
                        {max: 5, message: '长度最大5位', trigger: 'blur'},
                    ],
                },
            },
            category_form: {
                labelCol: {span: 6},
                wrapperCol: {span: 14},
                other: '',
                form: {
                    category: '',
                },
                category_rules: {
                    category: [{required: true, message: '请输入类别', trigger: 'change'}],
                },
            },
            excel_model_visible: false, // 批量导入单板的窗口显示和隐藏
            excel_fileList: [],  // 等待上传的xls文件列表
            excel_uploading: false, // 显示当前上传文件组件是否属于上传文件过程中的状态
            default_password: "",   // 默认上传的单板列表的通用登录密码
            upload_excel_form: this.$form.createForm(this, {name: 'coordinated'}),
        }

    },
    created() {
        // ajax获取数据
        this.get_categorys()
        this.get_device_list()
    },
    methods: {
        showExcelModal() {
            // 显示批量上传单板的窗口
            this.excel_model_visible = true
        },
        handleUploadExcelCancel() {
            // 关闭批量上传单板的窗口
            this.excel_model_visible = false;
        },
        beforeExcelUpload(file) {
            // 当用户选择上传文件以后，需要手动把当前文件添加到待上传文件列表this.excel_fileList中
            this.excel_fileList = [...this.excel_fileList, file];
            return false;
        },
        handleExcelRemove(file) {
            // 当用户要删除待上传文件列表中指定的文件时
            const index = this.excel_fileList.indexOf(file);
            const newFileList = this.excel_fileList.slice();
            newFileList.splice(index, 1);
            this.excel_fileList = newFileList;
        },
        handleExcelUpload(e) {
            // 上传execl文件的处理函数
            console.log("excel_fileList =", this.excel_fileList)
            // 整理要上传到服务端的数据对象[上传文件列表和默认密码]
            const formData = new FormData();
            this.excel_fileList.forEach(file => {
                formData.append('device[]', file);
            });
            formData.append("default_password", this.default_password)
            this.excel_uploading = true;
            // ajax提交
            let token = sessionStorage.token || localStorage.token;
            this.$axios.post(`/device/device_excel`, formData, {
                headers: {
                    Authorization: "jwt " + token
                }
            }).then(response => {
                // 把本地的单板列表数组和服务端返回的数组列表进行合并产生一个新的单板列表数组
                this.data = this.data.concat(response.data.data);
                this.excel_uploading = false; // 退出登录处理状态
                this.$message.success('上传成功');
                if (response.data.error.length > 0) {
                    this.$message.error('上传的数据有存在错误！');
                } else {
                    this.excel_model_visible = false;
                }
            }).catch(error => {
                this.excel_uploading = false;
                this.$message.error('上传文件处理失败！');
            })
        },
        get_device_list() {
            let token = sessionStorage.token || localStorage.token || "";
            // 获取单板列表
            this.$axios.get(`/device/detail/`, {
                headers: {
                    Authorization: "jwt " + token,
                }
            }).then(response => {
                this.data = response.data
            }).catch(error => {
                this.$message.error("单板列表获取失败！")
            })
        },
        get_categorys() {
            // 获取单板类别
            let token = sessionStorage.token || localStorage.token || "";
            this.$axios.get(`/device/categorys/`, {
                headers: {
                    Authorization: "jwt " + token,
                }
            }).then(response => {
                this.categorys = response.data
            }).catch(error => {
                this.$message.error("单板类别获取失败！")
            })
        },
        handleSelectChange(value) {
            console.log(value);
        },
        showadddevicecaterage() {
            // 显示添加单板类别的表单窗口
            this.visible_type = true;
        },
        showModal() {
            // 显示添加单板的表单窗口
            this.visible = true;
        },
        handleCancel_category(e) {
            // 表单取消
            this.resetForm(); //清空表单内容

            this.visible_type = false; // 关闭对话框
        },
        handleCancel(e) {
            // 表单取消
            this.resetForm(); //清空表单内容

            this.visible = false; // 关闭对话框
        },
        onSubmit() {
            this.$refs.ruleForm.validate(valid => {
                // 验证通过则发送请求
                if (valid) {
                    let token = sessionStorage.token || localStorage.token || "";
                    // 将数据提交到后台进行保存，但是先进行连接校验，验证没有问题，再保存
                    this.$axios.post(`${this.$settings.device}/device/list/`, {
                            "name": this.device_form.form.name,
                            "category": this.device_form.form.category,
                            "ip_addr": this.device_form.form.ip_addr,
                            "description": this.device_form.form.description,
                            "port": this.device_form.form.port,
                            "username": this.device_form.form.username,
                            "password": this.device_form.form.password,
                        },
                        {
                            headers: {
                                Authorization: "jwt " + token,
                            }
                        }).then(response => {
                        // 在现有的单板列表，追加新增的单板列表
                        this.data.unshift(response.data);
                        this.handleCancel();
                    }).catch(error => {
                        this.$message.error("添加单板失败！");
                    })

                } else {
                    // 验证失败！
                    return false;
                }
            });
        },
        onSubmit_category() {
            this.$refs.ruleForm.validate(valid => {
                // 验证通过则发送请求
                if (valid) {
                    let token = sessionStorage.token || localStorage.token || "";
                    // 将数据提交到后台进行保存，但是先进行连接校验，验证没有问题，再保存
                    this.$axios.post(`${this.$settings.host}/device/categorys/`, {
                            "category": this.category_form.form.category,
                        },
                        {
                            headers: {
                                Authorization: "jwt " + token,
                            }
                        }).then(response => {
                        // 在现有的单板列表，追加新增的单板类别列表
                        this.data.unshift(response.data);
                        this.handleCancel();
                    }).catch(error => {
                        this.$message.error("添加单板类别失败！");
                    })

                } else {
                    // 验证失败！
                    return false;
                }
            });
        },
        handleFileChange(info) {
            if (info.file.status !== 'uploading') {
                console.log(info.file, info.fileList);
            }
            if (info.file.status === 'done') {
                this.$message.success(`${info.file.name} 上传成功`);
            } else if (info.file.status === 'error') {
                this.$message.error(`${info.file.name} 上传失败`);
            }
        },
        resetForm() {
            // 重置添加单板的表单信息
            this.$refs.ruleForm.resetFields();
        },
    }
}
</script>

<style scoped>

</style>