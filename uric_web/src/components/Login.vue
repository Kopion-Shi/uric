<template>
	<div class="login box">
		<img src="../assets/login.jpg" alt="">
		<div class="login">
			<div class="login-title">
				<img src="../assets/login3.jpeg" alt="">
				<p>hello Uirc!</p>
			</div>
			<div class="login_box">
				<div class="title">
					<span>登录</span>
				</div>
				<div class="inp">
					<input v-model="username" type="text" placeholder="用户名" class="user">
					<input v-model="password" type="password" class="pwd" placeholder="密码">
					<div class="rember">
						<p>
							<input type="checkbox" class="no" v-model="remember"/>
							<span>记住密码</span>
						</p>

					</div>
					<button class="login_btn" @click="login">登录</button>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
export default {
  name: "Login",
  data(){
    return {
        remember: false, // 是否记住登录
        username:"",
        password:"",
    }
  },
  methods:{
    login(){
      this.$axios.post(`/users/login/`,{
        username: this.username,
        password: this.password,
      }).then((response)=>{
        // locatStorage或者sessionStorage中存储token
        // 先清空原有的token
        localStorage.removeItem("token");
        sessionStorage.removeItem("token");
        if(this.remember){
          // 记住登录
          localStorage.token = response.data.token;
        }else{
          sessionStorage.token = response.data.token;
        }
        // 跳转到首页
        let self=this;
        this.$success({
            title: 'uric系统提示',
            content: `登录成功！`,
            onOk(){
              self.$router.push("/uric");
            }
          })
        // 下一个页面，首页加载时验证token有效性
      }).catch(error=>{
          this.$message.error('用户名或者密码有误，请重新输入！');
      });
    },
  },
}
</script>
<style scoped>
.box{
    width: 100%;
    height: 100%;
    position: relative;
    overflow: hidden;
}
.box img{
    width: 100%;
    min-height: 100%;
}
.box .login {
    position: absolute;
    width: 500px;
    height: 400px;
    top: 0;
    left: 0;
    margin: auto;
    right: 0;
    bottom: 0;
    top: -338px;
}
.login .login-title{
    width: 100%;
    text-align: center;
}
.login-title img{
    width: 190px;
    height: auto;
}
.login-title p{
    font-family: PingFangSC-Regular;
    font-size: 18px;
    color: #fff;
    letter-spacing: .29px;
    padding-top: 10px;
    padding-bottom: 50px;
}
.login_box{
    width: 400px;
    height: auto;
    background: rgba(255,255,255,0.3);
    box-shadow: 0 2px 4px 0 rgba(0,0,0,.5);
    border-radius: 4px;
    margin: 0 auto;
    padding-bottom: 40px;
}
.login_box .title{
    font-size: 20px;
    color: #9b9b9b;
    letter-spacing: .32px;
    border-bottom: 1px solid #e6e6e6;
    display: flex;
    justify-content: space-around;
    padding: 50px 60px 0 60px;
    margin-bottom: 20px;
    cursor: pointer;
}
.login_box .title span:nth-of-type(1){
    color: #4a4a4a;
    border-bottom: 2px solid #396fcc;
}

.inp{
    width: 350px;
    margin: 0 auto;
}
.inp input{
    border: 0;
    outline: 0;
    width: 100%;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
}
.inp input.user{
    margin-bottom: 16px;
}
.inp .rember{
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    margin-top: 10px;
}
.inp .rember p:first-of-type{
    font-size: 12px;
    color: #4a4a4a;
    letter-spacing: .19px;
    margin-left: 22px;
    display: -ms-flexbox;
    display: flex;
    -ms-flex-align: center;
    align-items: center;
    /*position: relative;*/
}
.inp .rember p:nth-of-type(2){
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .19px;
    cursor: pointer;
}

.inp .rember input{
    outline: 0;
    width: 30px;
    height: 45px;
    border-radius: 4px;
    border: 1px solid #d9d9d9;
    text-indent: 20px;
    font-size: 14px;
    background: #fff !important;
}

.inp .rember p span{
    display: inline-block;
    font-size: 12px;
    width: 100px;
    /*position: absolute;*/
    /*left: 20px;*/
}
#geetest{
	margin-top: 20px;
}
.login_btn{
     width: 100%;
    height: 45px;
    background: #396fcc;
    border-radius: 5px;
    font-size: 16px;
    color: #fff;
    letter-spacing: .26px;
    margin-top: 30px;
}
.inp .go_login{
    text-align: center;
    font-size: 14px;
    color: #9b9b9b;
    letter-spacing: .26px;
    padding-top: 20px;
}
.inp .go_login span{
    color: #84cc39;
    cursor: pointer;
}
</style>