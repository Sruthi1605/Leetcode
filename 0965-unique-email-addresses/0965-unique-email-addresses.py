class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            cleaned_email = local + '@' + domain
            unique_emails.add(cleaned_email)
        return len(unique_emails)