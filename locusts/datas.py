# -*- coding: utf-8 -*-
# @Author  : 一蓑烟雨任平生
# @Time    : 2020/12/17 18:02
import cx_Oracle
import json
from public.logs import Log


class TestOracle(object):
    def __init__(self, user, pwd, host, db):
        self.connect = cx_Oracle.connect(user + '/' + pwd + '@' + host + '/' + db)
        self.cursor = self.connect.cursor()

    def select(self, sql):
        list = []
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        col_name = self.cursor.description
        for row in result:
            dict = {}
            for col in range(len(col_name)):
                key = col_name[col][0]
                value = row[col]
                dict[key] = value
            list.append(dict)
        js = json.dumps(list, ensure_ascii=False, indent=2, separators=(',', ':'))
        Log().info(f'返回字符串{js}')
        return js

    def disconnect(self):
        self.cursor.close()
        self.connect.close()

    def insert(self, sql):
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            Log().info('插入数据成功')
        except Exception as e:
            Log().error(f'捕获异常{e}')
        finally:
            self.disconnect()

    def update(self, sql):
        try:
            self.cursor.execute(sql)
            self.connect.commit()

        except Exception as e:
            Log().error(f'捕获异常{e}')
        finally:
            self.disconnect()

    def delete(self, sql):
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            Log().info('删除数据成功')
        except Exception as e:
            Log().error(f'捕获异常{e}')
        finally:
            self.disconnect()

if __name__ == '__main__':
    i = 872290479990660
    while i < 872290479990760:
        print(i)
        #商户表
        db = TestOracle('PAYADM','NjNmMzg5NjczOWE3','192.168.31.203','ORCL')
        sql = f'''INSERT INTO PAYADM.T_URM_MINF  ("MERC_ID", "USR_NO", "MERC_PROV", "MERC_CITY", "MERC_CITY_NM", "REG_PROV", "MERC_STS", "MERC_STSW", "MERC_CNM", "MERC_ABBR", "MERC_PY_ABBR", "SPC_PAY_ALIAS", "UP_MERC_ID", "UP_USR_NO", "CHN_REL_FLG", "MERC_TYP", "MERC_CLS", "THD_CD", "PSN_CRP_FLG", "MCC_CD", "MERC_TRD_DESC", "MERC_ATTR", "CRP_NM", "CRP_ID_TYP", "CRP_ID_NO", "PRIN_NM", "MGT_SCP", "CUS_MGR", "CUS_MGR_NM", "MERC_LVL", "CRED_LVL", "RCV_MAG_AMT", "REG_CAP_AMT", "STAF_NUM", "OPN_BUS_DT", "MERC_POP", "MERC_POS_CNT1", "MERC_POS_CNT2", "BUS_ULD_ATTR", "MGT_SECT", "MGT_RGN", "ORG_RGN_SCP", "ORG_NUM", "NEED_INV_FLG", "INV_MOD", "INV_TIT", "INV_MAIL_ADDR", "INV_MAIL_ZIP", "INV_MERC", "MERC_HOT_LIN", "REG_ID", "WEB_NM", "WEB_URL", "TAX_CERT_ID", "ICP_ID", "AIC_MEM_FLG", "MERC_SRC", "MERC_SRC_DESC", "RCMD_UNIT_CD", "RCMD_UNIT_NM", "CLR_FLG", "CLR_MERC", "MIN_RTN_AMT", "REG_ADDR", "BUS_ADDR", "CLR_AC", "CLR_AC_TYP", "FAX", "DPNM_TMS_FLG", "CRE_REF_NO", "UPD_REF_NO", "CI_NO", "APPR_RMK", "RFD_MOD", "RFD_FEE_PRC_MOD", "EFF_DT", "EXP_DT", "AGR_RMK", "CRE_ORG", "CRE_DT", "CRE_TM", "OA_CRE_OPR", "OA_RVW_OPR", "UI_CRE_OPR", "UI_RVW_OPR", "UPD_DT", "UPD_TM", "UPD_OPR", "UPD_EFF_DT", "SPEC_RSC", "TM_SMP", "MKM_REB_RAT", "MERC_EFF_DT", "MERC_AGR_TYP", "ORG_CD", "ORG_COD", "BUSINESS_LICENSE", "MCC_SUB_CD", "IS_SP_PHC", "AC_NO", "AC_TYP", "ORG_NO", "MERC_CITY_REG", "MERC_ENM", "UP_MERC_NM", "TAX_REG_NO", "REG_ORG_NM", "BUS_ZIP", "HOL_BUS_FLG", "BUS_STR_HOUR", "BUS_END_HOUR", "BUS_AREA", "NMGT_SCP", "EST_MON_AMT", "RES_MGR_NM", "MERC_TXN_TYP", "MERC_PAY_TYP", "CATEGORY_ID", "MERC_CHK_ADDR", "MERC_CHK_ZIP", "MERC_CHK_COMM", "MERC_CHK_EMAIL", "MERC_CHK_FAX", "POS_BUS_TYP", "POS_DST_FLG", "MERC_POS_AD", "MERC_MOD_INF", "MERC_TXN_CLS", "EMV_FLG", "CDT_TXN_FLG", "CRDT_TXN_LMT", "MERC_OPR_ID", "MERC_OPR_MBL", "MERC_FM_FLG", "CHG_FEE_TYP", "AGT_MERC_ID", "AGT_MERC_NM", "AGT_MERC_IMG", "AGT_MERC_LVL", "OPR_MNG_ID", "OPR_MNG_NM", "MERC_DPS_AMT", "MERC_BOND_AMT", "MERC_BOND_REC", "MERC_DPS_REC", "MERC_DBA_DT", "ORG_IN_NO", "CRP_ABOVE_IMG", "CRP_BELOW_IMG", "BUS_LIC_IMG", "MERC_ATT_URL", "MERC_ATT_NAME", "ADD_FLG", "MERC_CORG_NM", "FREE_DES", "BIG_FLG", "BUS_CRP_TYP", "FEE_ORG_NO", "SALE_TYE", "BUS_WAY", "ADD_WAY", "COP_WITH_POP", "PER_CRT", "BUS_LIC_VLD", "BUS_LIC_EXP", "PER_CRT_VLD", "PER_CRT_EXP", "AGT_MERC_ATTR", "UP_AGT_MERC_ID", "AGT_MERC_STS", "AGT_BOND_AMT", "MERC_TRD_CLS", "POS_NUM", "PSAM_NUM", "ZONE_FLG", "BUS_LIC", "ICP_VAL", "CRP_ID_VAL", "PRIN_ID", "ORGN_COD", "HOD_NM", "HOD_ID_TYP", "HOD_ID", "HOD_ID_VAL", "SAFE_LV", "BUS_LIC_EXP_DT", "ORGN_COD_EXP_DT", "UNI_MERC_CITY", "NOD_ID", "STL_DAT_TYP", "MCC_SP_CD", "ZIP_FIL_PATH", "LEA_CONT_IMG", "MERC_FEE_TYPE", "WXPAY_FLG", "WXPAY_SUB_MECH_ID", "REVIEW_STS", "REVIEW_RMK", "REG_EXP_DT", "ORG_EXP_DT", "TAX_EXP_DT", "CRP_EXP_DT", "CLAR_MERC", "PRV_FLG", "GRP_ID", "ALIPAY_SUB_MECH_ID", "ALIPAY_FLG", "MERC_MBL", "UNPAY_FLG", "REVOKE_DT", "REVOKE_TM", "MCC_SUB_CD_1", "LHHY_FLG", "INET_MERC_ID", "ITEM_ID", "SHOP_ID", "INET_MERC_NM", "LOCK_RMK", "UNLOCK_RMK", "PROXY_NM", "PROXY_CERT_TYPE", "PROXY_CERT_NO", "PROXY_CERT_EXP_DT", "PROXY_PHONE", "MERC_COUNTY", "POOL_FLG", "WX_ITEM", "ALI_ITEM", "FROM_TYP", "AGT_ID", "PAYMENT_FLG", "SPE_FLG", "CHK_TYP", "SEC_STL_SIGN", "FOT_MERC_ID", "BILL_SIGN", "IS_MULT_BANK_ACC", "JSAPP_FLG", "SPC_FLG", "SPC_EFF_DT", "SPC_EXP_DT", "ACQ_STL_SIGN", "ACQ_OPN_BNK_DESC", "ACQ_BNK_ACNM", "ACQ_STL_OAC", "SPC_TYP", "D_ZERO_FLG", "D_EFF_TM", "REP_CHANNEL", "UNFREEZE_DT", "ALI_FEE_TYP", "WX_FEE_TYP", "EMAIL_ENABLE", "ALI_JSAPP_FLG", "AGT_NO", "LST_TRS_TM", "RC_REMARK", "RC_TRADE_TYPE", "RC_TRD_CURB_BEG_DT", "RC_TRD_CURB_END_DT", "RC_SETTLE_TYPE", "RC_SETTLE_CURB_BEG_DT", "RC_SETTLE_CURB_END_DT", "OUT_MERC_ID", "LZPAY_FLG") VALUES ({i}, '110000601843', '2900', '2900', ' ', ' ', '0', '000000000000000', '菜信网', '菜信网', ' ', ' ', ' ', '0', '0', '3', '0', ' ', '1', '7999', ' ', '11', 'F1317A8DD5E5558F1112EB95B0460AA8', '00', '574282666AADDB13CD0E9B122C9D4639B7CEE8C4B1A69AFF82C90EC09D70F0C8', ' ', ' ', '162', ' ', '0', '5', '0', '0', '0', ' ', ' ', '0', '0', ' ', '1', '1', ' ', '0', 'N', '1', ' ', ' ', ' ', ' ', ' ', NULL, ' ', ' ', NULL, ' ', ' ', '1', ' ', ' ', ' ', '0', '872290479990169', '0', ' ', '上海市', '8000030000106713767', '800', ' ', ' ', ' ', ' ', '0', ' ', ' ', '0', ' ', '20251110', ' ', '0', '20201110', '142437', ' ', ' ', 'T00125', 'T00125', '20201110', '142437', ' ', ' ', ' ', '20201110142437', '100', ' ', '0', '0990000001', NULL, NULL, '014', NULL, '8000030000106713767', '800', '0990000001', ' ', ' ', ' ', ' ', ' ', ' ', 'Y', ' ', ' ', ' ', ' ', '0', ' ', ' ', ' ', '0', ' ', ' ', ' ', 'xiao.mingxian@chinaebi.com', ' ', ' ', ' ', ' ', ' ', ' ', 'N', ' ', '0', ' ', ' ', '0', NULL, ' ', ' ', ' ', ' ', ' ', ' ', '0', '0', '0', '0', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '2', ' ', ' ', 'N', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '0', '7999', '0', '0', NULL, '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', '01', NULL, ' ', '01', NULL, 'data/merc/20201110/162099909990113.zip', NULL, '1', 'Y', NULL, NULL, NULL, ' ', ' ', ' ', '20250930', NULL, '3', NULL, NULL, 'Y', 'BD144F66FE7CD4D1B1ABA000BE72F967', 'Y', ' ', ' ', '014035', 'N', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2904', '0', NULL, NULL, '02', '162', 'Y', ' ', '01', '0', NULL, '1', '0', 'N', NULL, NULL, NULL, '1', NULL, '菜信网', '6226095950521497', NULL, '0', NULL, NULL, NULL, NULL, NULL, '1', 'N', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '90998773100928', 'N')'''
        db.insert(sql)
        # db = TestOracle('PAYADM','NjNmMzg5NjczOWE3','192.168.31.203','ORCL')
        # sql = f'''select * from PAYADM.T_URM_MINF where MERC_ID = {i}'''
        # db.select(sql)
        #结算表
        db = TestOracle('PAYADM','NjNmMzg5NjczOWE3','192.168.31.203','ORCL')
        sql = f'''INSERT INTO payadm.t_urm_mstl ("MERC_ID", "EFF_DT", "EXP_DT", "USR_NO", "MERC_STL_FLG", "STL_MOD", "PAS_STL_FLG", "STL_PERD", "STL_DAY", "STL_DAY_BIT", "STL_TRF_DAYS", "STL_BEG_AMT", "MIN_RTN_AMT", "LAST_STL_DT", "NEXT_STL_DT", "STL_CLS", "AMT_TYP", "STL_OAC", "STL_OAC_CLS", "BNK_ACNM", "WC_LBNK_NO", "OPN_BNK_PROV", "OPN_BNK_CITY", "OPN_BNK_DESC", "EFF_FLG", "UPD_DT", "UPD_TM", "UPD_TLR", "TM_SMP", "STL_SIGN", "BNK_TYP", "WC_BNK", "NEXT_STL_TM", "LAST_STL_TM", "STL_END_TM", "STL_SELF_FLG", "FEE_IAC_TYP", "FEE_IN_AC", "STL_OAC_SEC", "WC_LBNK_NO_SEC", "BNK_ACNM_SEC", "PRE_MERC_STL_FLG", "PRE_STL_PERD", "STL_UP_ACTIVE_DT", "PRE_STL_TRF_DAYS", "PRE_STL_OAC_CLS") VALUES ('{i}', '20190302', '20211110', '110000601843', '0', '0', '0', 'D', '0', NULL, '1', '0', '0', '20200605', '20201110', '2', '1', '75BB7688FB8D0AEDD48B8BE4FBEF95D54CF3147FE8A3980785A42D90CE5A82AA', '4', 'F1317A8DD5E5558F1112EB95B0460AA8', '102110010037', NULL, NULL, NULL, '1', '20201116', '103202', 'T00020', '20201116103202', '1', NULL, NULL, NULL, NULL, NULL, '0', '806', '8060030000106713787', NULL, NULL, NULL, '0', 'D', '20201117', '1', '4')'''
        db.insert(sql)
        #终端表
        db = TestOracle('PAYADM','NjNmMzg5NjczOWE3','192.168.31.203','ORCL')
        sql = f'''INSERT INTO payadm.t_tms_pos("MERC_ID", "TRM_NO", "TRM_SN", "MFR_NO", "MOD_NO", "TRM_STS", "SGN_STS", "TRM_OWN", "TRM_TYP", "TRM_NM", "INS_AD", "INS_DT", "BEG_DT", "PM_DW_FLG", "EMV_DW_FLG", "PER_CCY", "DPS_AMT", "CONN_MOD", "EMV_PM_MOD", "PRV_FLG", "RARD_CD", "BAT_NO", "ORG_NO", "TRM_KEY", "TRM_TEK", "TRM_SEK", "MAC_KEY", "PIN_KEY", "RFD_FLG", "SFT_VER", "OFF_FLG", "SIG_DT", "RSV_DAT", "UPD_DT", "UPD_TLR", "TM_SMP", "REG_DT", "TRM_PROV", "TRM_CITY", "BAT_CHK_FLG", "POL_WEEK", "POL_DT", "MAI_MGR", "SVR_OWE", "MTH_OWE", "TELL_NO", "SIM_NO", "OPEN_CTT_PSN_CNM", "OPEN_MBL_TEL", "DAY_DLIMIT", "DAY_CLIMIT", "HARDWARE_NUM", "PHONE_ID", "LG_LAT_TUDE", "POS_KEY", "TRACK_KEY", "STORE_ID", "MGR_DESFLG", "KEK2_CHECK_VALUE", "MGR_KEY_INDEX", "LST_UPD_TLR", "SHA_KEY", "TRM_COUNTY", "LAT", "LON", "SIGN_TYP") VALUES ({i}, '08267261', 'HH1131039', '532', '9844', 'Y', '0', '0', '0', ' ', '上海市', '20201111', ' ', '0', '11', '0', '0', ' ', ' ', '3', '2900', '000001', '0990000001', 'EFEB491C971331FC39103A53A395D2DE', 'EFEB491C971331FC39103A53A395D2DE', 'AB27A56A192FA8F0F7ECF73BA480A283', ' ', ' ', '1', ' ', '0', ' ', ' ', '20201111', 'T00203', '20201111145103', '20201111', '2900', '2900', '1', '0', '20201111', NULL, '0', '0', NULL, '13212312322', '上海市', '13212312312', '0', '0', ' ', ' ', ' ', '88888888', NULL, '00002', NULL, '5AB62606F8D0C33B', NULL, NULL, NULL, NULL, '31.405270', '121.489410', '0')'''
        db.insert(sql)
        # sql = f'''select * from payadm.t_urm_mstl where MERC_ID = {i}'''
        # db.select(sql)
        #权限表
        db = TestOracle('CSDBPG','NDc5ZTc4YzYyNTcx','192.168.31.203','ORCL')
        sql = f'''INSERT INTO csdbpg.T_CGW_UPAPCNF_NET("MERC_ID", "REG_MERC_ID", "CNL_TYPE", "CNL_NAME", "PAY_TYPE", "MCH_ID", "SUB_MCH_ID", "SUB_APP_ID", "SUB_OPENID", "CHANNEL_ID", "COOP_ORG", "TM_SMP", "INCOME_TYP", "ORIGINAL_ID") VALUES ('{i}', '{i}', 'AL', '支付宝通道', '03', '2017040606571877', '2088010352038783', NULL, NULL, NULL, 'CUP', '20201110142444', NULL, NULL)'''
        db.insert(sql)
        # db = TestOracle('CSDBPG','NDc5ZTc4YzYyNTcx','192.168.31.203','ORCL')
        # sql = f'''select * from csdbpg.T_CGW_UPAPCNF_NET where MERC_ID = {i}'''
        # db.select(sql)
        i += 1

