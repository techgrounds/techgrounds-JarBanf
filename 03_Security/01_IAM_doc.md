# IAM
An organization's IT department needs a way to control what users can and can't access so that sensitive data and functions are restricted to only the people and things that need to work with them. This is where identity and access management (IAM) comes in.  

IAM gives secure access to company resources, like emails, databases, data, and applications, to verified entities. The goal is to manage access so that the right people can do their jobs and the wrong people, like hackers, are denied entry.

With an IAM system, an organization can quickly and accurately verify a person's identity and that they have the necessary permissions to use the requested resource during each access attempt.

## Key-terms


## Assignment
Study:
1. The difference between authentication and authorization.
2. The three factors of authentication and how MFA improves security.
3. What the principle of least privilege is and how it improves security.

### Used sources
- [What is identity and access management (IAM)?](https://www.microsoft.com/en-us/security/business/security-101/what-is-identity-access-management-iam)
- [Meaning of authentication in English](https://dictionary.cambridge.org/dictionary/english/authentication)
- [Meaning of authorization in English
](https://dictionary.cambridge.org/dictionary/english/authorization)
- [Difference between Authentication and Authorization](https://www.geeksforgeeks.org/difference-between-authentication-and-authorization/)
- [MFA](https://csrc.nist.gov/glossary/term/mfa)
- [What is Multi-Factor Authentication (MFA)?](https://aws.amazon.com/what-is/mfa/)
- [What is the Principle of Least Privilege (POLP)?](https://www.digitalguardian.com/blog/what-principle-least-privilege-polp-best-practice-information-security-and-compliance)

### Encountered problems
None

### Result
**1. The difference between authentication and authorization.**

<ins>Cambridge dictionary</ins>  
- **authentication**: the process of proving that something is real, true, or what people say it is.
- **authorization**: official permission for something to happen, or the act of giving someone official permission to do something  

<ins>In IT</ins>  
- **authentication process**: the identity of users is checked for providing the access to the system.
- **authorization process**: a user's authorities/permissions are checked for accesing the resources.

Authentication process is done before the authorization process.  
Authorization process is done after the authentication process.

**2. The three factors of authentication and how MFA improves security.**

MFA, Multi Factor Authentication, is an authentication system that requires more than one distinct authentication factor for succesful authentication.  
The three authentication factors are: 
- **Knowledge factor**: something you know  
(password/personal identification number [PIN], answer to a secret question).
- **Possession factor**: something you have  
(mobile phone, security token).
- **Inherence factor**: something you are  
(fingerprint/retina scan, voice/facial recognition, behavior biometrics like keystrokes dynamics).

MFA acts as an additional layer of security to prevent unauthorized users from accessing an account, even when the password has been stolen.

**3. What the principle of least privilege is and how it improves security.**

The principle of least privilege (PoLP) is an information security concept which maintains that a user or entity should only have access to the specific data, resources and applications needed to complete a required task.

It works by limiting the accessible data, resources and application functions to only that which a user or entity requires to execute their specific task or workflow.

The less access a company allows to specific data, resources and applications, the smaller the odds that some malicious party will steal a legitimate user's credentials and use them to steal that specific data, resources and application.